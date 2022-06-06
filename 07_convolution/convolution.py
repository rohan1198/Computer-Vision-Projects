import numpy as np
import matplotlib.pyplot as plt

from numpy import ndarray
from typing import Tuple


def pad_image(img: ndarray, 
              padding: Tuple[int, int]) -> ndarray:
    _, w = img.shape
    rows, cols = padding

    padded_img = np.zeros((w + rows * 2, w + cols * 2))
    padded_img[rows: w + rows, cols: w + cols] = img

    return padded_img


def conv2d(img: ndarray, 
           kernel: ndarray, 
           stride: Tuple[int, int] = (1, 1), 
           dilation: Tuple[int, int] = (1, 1), 
           padding: Tuple[int, int] = (0, 0)) -> ndarray:
    
    if not isinstance(img, np.ndarray):
        img = np.array(img)

    h, w = img.shape

    img = img if list(padding) == [0, 0] else pad_image(img, padding)

    if not isinstance(kernel, np.ndarray):
        kernel = np.array(kernel)

    h_out = np.floor((h + 2 * padding[0] - kernel.shape[0] - (kernel.shape[0] - 1)
                     * (dilation[0] - 1)) / stride[0]).astype(int) + 1
    w_out = np.floor((w + 2 * padding[1] - kernel.shape[1] - (kernel.shape[1] - 1)
                     * (dilation[1] - 1)) / stride[1]).astype(int) + 1

    out_mat = np.zeros((h_out, w_out))

    kernel_center = kernel.shape[0] // 2, kernel.shape[1] // 2

    new_center_x = kernel_center[0] * dilation[0]
    new_center_y = kernel_center[1] * dilation[1]

    for i in range(h_out):
        center_x = new_center_x + i * stride[0]
        idx_x = [center_x + l * dilation[0]
                     for l in range(-kernel_center[0], kernel_center[0] + 1)]

        for j in range(w_out):
            center_y = new_center_y + j * stride[1]
            idx_y = [center_y + l * dilation[1]
                         for l in range(-kernel_center[1], kernel_center[1] + 1)]

            sub_mat = img[idx_x, :][:, idx_y]

            out_mat[i][j] = np.sum(np.multiply(sub_mat, kernel))

    return out_mat


def plot(img1: np.ndarray, img2: np.ndarray, op: str) -> None:
    _, ax = plt.subplots(1, 2, sharex=False, sharey=False)
    ax[0].imshow(img1, cmap="gray")
    ax[0].set_title("Original Image")

    ax[1].imshow(img2, cmap="gray")
    ax[1].set_title(f"Convolved Image ({op})")

    plt.show()
