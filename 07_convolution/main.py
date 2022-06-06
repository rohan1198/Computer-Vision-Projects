import cv2
import argparse
import numpy as np

from convolution import conv2d, plot


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="Path to the input image")
    parser.add_argument(
        "--kernel",
        type=str,
        default="blur",
        choices=[
            "identity",
            "blur3",
            "blur5",
            "sharpen",
            "outline",
            "unsharp"],
        help="Type of kernel")
    parser.add_argument(
        "--stride",
        nargs="+",
        type=int,
        default=[1,1],
        help="Stride")
    parser.add_argument(
        "--padding",
        nargs="+",
        type=int,
        default=[0,0],
        help="Padding")
    parser.add_argument(
        "--dilation",
        nargs="+",
        type=int,
        default=[1,1],
        help="Dilation")

    args = parser.parse_args()

    img = cv2.imread(args.path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if args.kernel == "identity":
        kernel = np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]])

    elif args.kernel == "blur3":
        kernel = np.array([[1, 2, 1],
                           [2, 4, 2],
                           [1, 2, 1]]) / 16

    elif args.kernel == "blur5":
        kernel = np.array([[1, 4, 6, 4, 1],
                           [4, 16, 24, 16, 4],
                           [6, 24, 36, 24, 6],
                           [4, 16, 24, 16, 4],
                           [1, 4, 6, 4, 1]]) / 256

    elif args.kernel == "sharpen":
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

    elif args.kernel == "unsharp":
        kernel = np.array([[1, 4, 6, 4, 1],
                           [4, 16, 24, 16, 4],
                           [6, 24, -476, 24, 6],
                           [4, 16, 24, 16, 4],
                           [1, 4, 6, 4, 1]]) / 256

    elif args.kernel == "outline":
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])

    convolved_img = conv2d(img, 
                           kernel, 
                           tuple(args.stride), 
                           tuple(args.dilation), 
                           tuple(args.padding))

    plot(img, convolved_img, args.kernel)
