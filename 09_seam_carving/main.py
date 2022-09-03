import sys
import cv2
import argparse
import matplotlib.pyplot as plt

from utils import crop_col, crop_row



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--path", type = str, required = True, help = "Path to the image")
    parser.add_argument("--axis", type = str, choices = ['row', 'col'], default = "col", help = "Resize horizontally or vertically")
    parser.add_argument("--scale", type = float, default = 0.8, help = "New image scale")
    parser.add_argument("--out", type = str, default = "output.jpg", help = "Name of the output file")

    args = parser.parse_args()

    img = cv2.imread(args.path)

    if args.axis == "row":
        out = crop_row(img, args.scale)
    elif args.axis == "col":
        out = crop_col(img, args.scale)
    else:
        print("Please choose either ['row', 'col']")
        sys.exit(1)
    
    cv2.imwrite(args.out, out)

    fig, ax = plt.subplots(1, 2, sharex = True)
    ax[0].imshow(img)
    ax[0].set_title(f"Original image: ({img.shape})")
    ax[0].axis("off")

    ax[1].imshow(out)
    ax[1].set_title(f"Seam Carved image: ({out.shape})")
    ax[1].axis("off")

    fig.tight_layout()
    
    plt.show()
