import numpy as np
import matplotlib.pyplot as plt

from numba import jit
from tqdm import trange
from typing import Union
from numpy import ndarray
from scipy.ndimage import convolve


def calculate_energy(img: ndarray) -> ndarray:
    sobelx = np.array([[ 1.0,  2.0,  1.0],
                       [ 0.0,  0.0,  0.0],
                       [-1.0, -2.0, -1.0],
                       ])
    
    sobely = np.array([[1.0, 0.0, -1.0],
                       [2.0, 0.0, -2.0],
                       [1.0, 0.0, -1.0],
                       ])

    # Adds a channel dimension, changing it from (3, 3) to (3, 3, 3)
    sobelx3d = np.stack([sobelx] * 3, axis = 2)
    sobely3d = np.stack([sobely] * 3, axis = 2)

    img = img.astype("float32")
    convolved = np.absolute(convolve(img, sobelx3d)) + np.absolute(convolve(img, sobely3d))

    energy_map = convolved.sum(axis = 2)

    #plt.figure()
    #plt.imshow(energy_map, cmap = "gray")
    #plt.title("Energy Map of the input image")
    #plt.axis("off")
    #plt.show()

    return energy_map


@jit
def minimum_seam(img: ndarray) -> Union[ndarray, ndarray]:
    h, w, _ = img.shape
    energy_map = calculate_energy(img)

    M = energy_map.copy()
    backtrack = np.zeros_like(M, dtype = int)

    for i in range(1, h):
        for j in range(1, w):
            if j == 0:    # Left edge of the image
                idx = np.argmin(M[i - 1, j: j + 2])
                backtrack[i, j] = idx + j
                min_energy = M[i - 1, idx + j]
            else:
                idx = np.argmin(M[i - 1, j - 1:j + 2])
                backtrack[i, j] = idx + j - 1
                min_energy = M[i - 1, idx + j - 1]
            
            M[i, j] += min_energy
    
    return M, backtrack


@jit
def carve_column(img: ndarray) -> ndarray:
    h, w, _ = img.shape

    M, backtrack = minimum_seam(img)
    mask = np.ones((h, w), dtype = bool)

    j = np.argmin(M[-1])

    for i in reversed(range(h)):
        mask[i, j] = False
        j = backtrack[i, j]
    
    mask = np.stack([mask] * 3, axis = 2)
    img = img[mask].reshape((h, w - 1, 3))

    return img


def crop_col(img: ndarray, scale: float) -> ndarray:
    _, w, _ = img.shape
    new_w = int(scale * w)

    for _ in trange(w - new_w):
        img = carve_column(img)

    return img


def crop_row(img: ndarray, scale: float) -> ndarray:
    img = np.rot90(img, 1, (0, 1))
    img = crop_col(img, scale)
    img = np.rot90(img, 3, (0, 1))

    return img
