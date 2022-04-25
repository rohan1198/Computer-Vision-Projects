import cv2
import argparse
import matplotlib.pyplot as plt
from numpy import ndarray


def simple_equalization(img: ndarray) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with (h, w)"
    equalized_img = cv2.equalizeHist(img)

    return equalized_img


def adaptive_equalization(
    img: ndarray,
    clip: float = 2,
    grid: tuple = (8, 8)) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with (h, w)"

    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(grid, grid))
    equalized_img = clahe.apply(img)

    return equalized_img


def show(rgb_img: ndarray, gray_img: ndarray, eq_img: ndarray) -> None:
    _, ax = plt.subplots(1, 3, sharex=False, sharey=False)
    ax[0].imshow(rgb_img)
    ax[0].set_title("original image")

    ax[1].imshow(gray_img, cmap=plt.set_cmap("gray"))
    ax[1].set_title(f"grayscale image")

    ax[2].imshow(eq_img, cmap=plt.set_cmap("gray"))
    ax[2].set_title(f"equalized image")

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path to the input image")
    parser.add_argument(
        "--method",
        type=str,
        choices=["simple", "adaptive"],
        default="adaptive",
        help="Equalization method to apply")
    parser.add_argument(
        "--clip", 
        type=float, 
        default=40,
        help="Threshold for contrast limiting")
    parser.add_argument(
        "--grid", 
        type=int, 
        default=8,
        help="Size of the grid (nxn)")

    args = parser.parse_args()

    img = cv2.imread(args.path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if args.method == "simple":
        equalized_img = simple_equalization(gray_img)

    elif args.method == "adaptive":
        equalized_img = adaptive_equalization(gray_img, args.clip, args.grid)

    show(img, gray_img, equalized_img)
