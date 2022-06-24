import cv2
import yaml
import numpy as np
import argparse
import matplotlib.pyplot as plt

from numpy import ndarray


def correct_image(args) -> ndarray:
    with open("./params.json", "r") as f:
        try:
            params = yaml.safe_load(f)

            ret = np.array(params["ret"])
            mat = np.array(params["mat"])
            dist = np.array(params["dist"])
            rvecs = np.array(params["rvecs"])
            tvecs = np.array(params["tvecs"])
        
        except yaml.YAMLError as e:
            print(e)

    img = cv2.imread(args.path)
    h, w = img.shape[:2]

    new_camera_mat, roi = cv2.getOptimalNewCameraMatrix(cameraMatrix = mat,
                                                        distCoeffs = dist,
                                                        imageSize = (w, h),
                                                        alpha = 1,
                                                        newImgSize = (w, h)
                                                        )
    
    dst = cv2.undistort(img, mat, dist, None, new_camera_mat)

    x, y, w, h = roi
    dst = dst[y: y + h, x: x + w]

    w, h = img.shape[:2]

    resized_img = cv2.resize(dst, (h, w), interpolation = cv2.INTER_AREA)

    if args.vis:
        plt.figure(figsize = (12, 8))
        fig, ax = plt.subplots(1, 2, sharex=False, sharey=False)
        ax[0].imshow(img)
        ax[0].set_title("Original Image")
        ax[0].axis("off")

        ax[1].imshow(resized_img)
        ax[1].set_title(f"Corrected Image")
        ax[1].axis("off")
        
        if args.save:
            plt.savefig("vis.jpg")
        
    plt.show()

    return resized_img



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type = str, required = True, help = "Path to the image")
    parser.add_argument("--params", type = str, default = "calibration_params", help = "Path to the calibration parameters")
    parser.add_argument("--vis", action = "store_true", help = "View original and calibrated images")
    parser.add_argument("--save", action = "store_true", help = "Save the output")

    args = parser.parse_args()

    if args.save:
        calibrated_img = correct_image(args)
        cv2.imwrite('output.jpg', calibrated_img)