import argparse
import cv2

from numpy import ndarray
from sklearn.cluster import MiniBatchKMeans


def quantize(img: ndarray) -> ndarray:
    (height, width) = img.shape[:2]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)    # Convert to LAB colour space
    img = img.reshape(img.shape[0] * img.shape[1], 3)    # feature vector

    cluster = MiniBatchKMeans(n_clusters=args.levels)
    labels = cluster.fit_predict(img)

    quant = cluster.cluster_centers_.astype("uint8")[labels]
    quant = quant.reshape((height, width, 3))
    quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)

    return quant


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="Path to the video")
    parser.add_argument(
        "--levels",
        type=int,
        default=4,
        help="Level of quantization (please provide a multiple of 2)")

    args = parser.parse_args()

    vid = cv2.VideoCapture(args.path)

    while True:
        ret, frame = vid.read()

        quant = quantize(frame)

        out = cv2.hconcat([frame, quant])

        cv2.imshow('frame', out)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()
