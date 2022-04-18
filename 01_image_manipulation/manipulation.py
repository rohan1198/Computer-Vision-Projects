import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray


def scale(img: ndarray, dim: tuple = (100, 100)) -> ndarray:
    scaled_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    return scaled_img


def rotate(img: ndarray, angle: int = 15) -> ndarray:
    (height, width) = img.shape[:2]
    center = (width / 2, height / 2)

    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, rot_mat, (width, height))

    return rotated_img


def translate(img: ndarray, shift: list = [10, 10]) -> ndarray:
    translated_mat = np.float32(
        [[1, 0, shift[0]], [0, 1, shift[1]]])  # type: ignore
    translated_img = cv2.warpAffine(
        img, translated_mat, (img.shape[1], img.shape[0]))

    return translated_img


def crop(
    img: ndarray, range_x: list = [
        100, 100], range_y: list = [
            100, 100]) -> ndarray:
    cropped_img = img[range_x[0]: range_x[1], range_y[0]: range_y[1]]

    return cropped_img


def show_images(
        image_1: ndarray,
        image_2: ndarray,
        transform: str = " ") -> None:
    _, ax = plt.subplots(1, 2, sharex=False, sharey=False)
    ax[0].imshow(image_1)
    ax[0].set_title("original image")

    ax[1].imshow(image_2)
    ax[1].set_title(transform)

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--img",
        type=str,
        default="../lena.jpg",
        help="Path to the input image")
    parser.add_argument(
        "--transform",
        type=str,
        default="scale",
        choices=[
            "scale",
            "rotate",
            "translate",
            "crop"],
        help="Select transformation to apply")
    parser.add_argument(
        "--dim",
        type=int,
        default=100,
        help="New image dimensions (dim, dim)")
    parser.add_argument(
        "--angle",
        type=int,
        default=15,
        help="Angle of rotation")
    parser.add_argument(
        "--translate",
        type=int,
        default=[
            10,
            10],
        nargs="+",
        help="Shift right and down respectively from the center")
    parser.add_argument(
        "--crop-x",
        type=int,
        default=[
            0,
            100],
        nargs="+",
        help="Range along x-axis")
    parser.add_argument(
        "--crop-y",
        type=int,
        default=[
            0,
            100],
        nargs="+",
        help="Range along y-axis")

    args = parser.parse_args()
    print(args)

    img = cv2.imread(args.img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if args.transform == "scale":
        scaled_img = scale(img, (args.dim, args.dim))

        show_images(img, scaled_img, args.transform)

        print("Original Image shape: ", img.shape)
        print("Scaled Image shape", scaled_img.shape)

    elif args.transform == "rotate":
        rotated_img = rotate(img, angle=args.angle)

        show_images(img, rotated_img, args.transform)

    elif args.transform == "translate":
        translated_img = translate(img, shift=(args.translate))

        show_images(img, translated_img, args.transform)

        print("Original Image shape: ", img.shape)
        print("Translated Image shape", translated_img.shape)

    elif args.transform == "crop":
        cropped_img = crop(img, args.crop_x, args.crop_y)

        show_images(img, cropped_img, args.transform)

        print("Original Image shape: ", img.shape)
        print("Cropped Image shape", cropped_img.shape)

    else:
        print(
            'Please choose an image operation from the list ["scale", "rotate", "translate", "crop"]')
        pass
