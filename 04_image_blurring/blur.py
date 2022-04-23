import cv2
import argparse
import matplotlib.pyplot as plt
from numpy import ndarray


def avg_blur(img: ndarray, kernel_size: int) -> ndarray:
    avg_blurred_img = cv2.blur(img, (kernel_size, kernel_size))

    return avg_blurred_img


def gaus_blur(img: ndarray, kernel_size: int) -> ndarray:
    gaus_blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    return gaus_blurred_img


def med_blur(img: ndarray, kernel_size: int) -> ndarray:
    med_blurred_img = cv2.medianBlur(img, kernel_size)

    return med_blurred_img


def bil_blur(
        img: ndarray,
        diameter: int = 11,
        colour: int = 61,
        space: int = 39) -> ndarray:
    bil_blurred_img = cv2.bilateralFilter(img, diameter, colour, space)

    return bil_blurred_img


def show(img1: ndarray, img2: ndarray, method = None) -> None:
    _, ax = plt.subplots(1, 2, sharex=False, sharey=False)
    ax[0].imshow(img1)
    ax[0].set_title("original image")

    ax[1].imshow(img2, cmap = plt.get_cmap("gray"))
    
    if method is not None:
        ax[1].set_title(f"blurred image ({method})")
    else:
        ax[1].set_title(f"blurred image")

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
        default="average",
        choices=[
            "average",
            "gaussian",
            "median",
            "bilateral"],
        help="Smoothing method to apply")
    parser.add_argument(
        "--kernel",
        type=int,
        default=3,
        help="Kernel size (nxn). Please provide an odd number input")
    parser.add_argument("--diameter", type=int, default=11,
                        help="Diameter of pixel neighbourhood")
    parser.add_argument("--colour", type=int, default=61,
                        help="Colour standard deviation")
    parser.add_argument("--space", type=int, default=39,
                        help="Space standard deviation")

    args = parser.parse_args()

    img = cv2.imread(args.path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if args.method == "average":
        blurred_img = avg_blur(img, args.kernel)

    elif args.method == "gaussian":
        blurred_img = gaus_blur(img, args.kernel)

    elif args.method == "median":
        blurred_img = med_blur(img, args.kernel)

    elif args.method == "bilateral":
        blurred_img = bil_blur(img, args.diameter, args.colour, args.space)

    else:
        print('Please choose one of the methods: ("average", "gaussian", "median", "bilateral")')

    show(img, blurred_img, args.method)
