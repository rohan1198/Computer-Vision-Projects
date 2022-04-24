import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray


def edge_detection(img: ndarray, low_thresh: int = 30,
                   high_thresh: int = 150) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with dimensions (h, w)"
    edge_img = cv2.Canny(img, low_thresh, high_thresh)

    return edge_img


# Reference: PyImageSearch
def auto_edge_detection(img: ndarray, sigma: float = 0.33) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with dimensions (h, w)"

    median_img = np.median(img)

    narrow_thresh = max(0, int((1.0 - sigma) * median_img))
    wide_thresh = min(255, int((1.0 + sigma) * median_img))

    edge_img = cv2.Canny(img, narrow_thresh, wide_thresh)

    return edge_img


def show(img1: ndarray, img2: ndarray) -> None:
    _, ax = plt.subplots(1, 2, sharex=False, sharey=False)
    ax[0].imshow(img1)
    ax[0].set_title("original image")

    ax[1].imshow(img2, cmap=plt.set_cmap("binary"))
    ax[1].set_title(f"edge map")

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path to the input image")
    parser.add_argument(
        "--low-thresh",
        type=int,
        default=30,
        help="Lower limit of the threshold")
    parser.add_argument(
        "--high-thresh",
        type=int,
        default=150,
        help="Higher limit of the threshold")
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Automatic thresholding")
    parser.add_argument(
        "--sigma",
        type=float,
        default=0.33,
        help="Threshold percentage")

    args = parser.parse_args()

    img = cv2.imread(args.path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if args.auto:
        edge_img = auto_edge_detection(gray_img, sigma=args.sigma)
    else:
        edge_img = edge_detection(
            gray_img,
            low_thresh=args.low_thresh,
            high_thresh=args.high_thresh)

    show(img, edge_img)
