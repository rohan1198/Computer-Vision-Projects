import cv2
import argparse
import matplotlib.pyplot as plt
from numpy import ndarray


def erosion(img: ndarray, iterations: int = 3) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with dimensions (h, w)"
    eroded_img = cv2.erode(img.copy(), None, iterations=iterations + 1)

    return eroded_img


def dilation(img: ndarray, iterations: int = 3) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with dimensions (h, w)"
    dilated_img = cv2.dilate(img.copy(), None, iterations=iterations + 1)

    return dilated_img


def opening(img: ndarray, kernel_size: tuple = (3, 3)) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with dimensions (h, w)"
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opened_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    return opened_img


def closing(img: ndarray, kernel_size: tuple = (3, 3)) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with dimensions (h, w)"
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return closed_img

def gradient(img: ndarray, kernel_size: tuple = (3, 3)) -> ndarray:
    assert len(
        img.shape) == 2, "Please make sure input is a grayscale image with dimensions (h, w)"
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    gradient_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return gradient_img


def show(img: ndarray, args) -> None:
    if args.op == "erosion" or args.op == "dilation":
        plt.figure()
        plt.subplots_adjust(hspace=0.5)
        plt.suptitle(args.op)
        plt.axis("off")

        for i, k in enumerate(range(0, args.iter)):
            ax = plt.subplot(1, args.iter, i + 1)

            if args.op == "erosion":
                processed_img = erosion(img, iterations=i)
            elif args.op == "dilation":
                processed_img = dilation(img, iterations=i)
            else:
                pass

            ax.imshow(processed_img, cmap=plt.get_cmap("gray"))
            ax.set_title(f"Iteration: {k + 1}")

        plt.show()

    elif args.op == "opening" or args.op == "closing":
        if args.op == "opening":
            processed_img = opening(
                img, kernel_size=(
                    args.kernel, args.kernel))
        elif args.op == "closing":
            processed_img = closing(
                img, kernel_size=(
                    args.kernel, args.kernel))
        else:
            pass

        _, ax = plt.subplots(1, 2, sharex=False, sharey=False)
        ax[0].imshow(img, cmap=plt.get_cmap("gray"))
        ax[0].set_title("Original")

        ax[1].imshow(processed_img, cmap=plt.get_cmap("gray"))
        ax[1].set_title(args.op)

        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--op",
        type=str,
        default="erosion",
        choices=[
            "erosion",
            "dilation",
            "opening",
            "closing"],
        help="Morphological Operation to perform")
    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path to the input image")
    parser.add_argument(
        "--iter",
        type=int,
        default=3,
        help="Number of times to perform the operation (only for erosion and dilation)")
    parser.add_argument(
        "--kernel",
        type=int,
        default=3,
        help="Kernel size (nxn) (only for opening and closing)")

    args = parser.parse_args()

    print("\n", args)

    img = cv2.imread(args.path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    show(gray_img, args)
