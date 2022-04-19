import argparse
import cv2
import matplotlib.pyplot as plt

from numpy import ndarray
from sklearn.cluster import MiniBatchKMeans


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


def quantize(img: ndarray, levels: int = 4) -> ndarray:
    (height, width) = img.shape[:2]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)    # Convert to LAB colour space
    img = img.reshape(img.shape[0] * img.shape[1], 3)    # feature vector

    cluster = MiniBatchKMeans(n_clusters=levels)
    labels = cluster.fit_predict(img)

    quant = cluster.cluster_centers_.astype("uint8")[labels]
    quant = quant.reshape((height, width, 3))
    quant = cv2.cvtColor(quant, cv2.COLOR_LAB2RGB)

    return quant


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="Path to the image")
    parser.add_argument(
        "--levels",
        type=int,
        default=4,
        help="Level of quantization (please provide a multiple of 2)")

    args = parser.parse_args()

    img = cv2.imread(args.path)

    quant = quantize(img , levels = args.levels)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    show_images(rgb_img, quant)