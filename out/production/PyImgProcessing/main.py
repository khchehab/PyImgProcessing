from PIL import Image
from processors.identity import Identity
from processors.edge_detection import EdgeDetection, EdgeDetectionType
from processors.gaussian_blur import GaussianBlur
from processors.sharpen import Sharpen
from model.kernel import Kernel
import math
import time

def main():
    print("Hello World!")
    img = "res/TajMahal.jpeg"

    # identity = Identity(img)
    # identity.apply_filter()
    # identity.display_filtered()

    # edgeDetection = EdgeDetection(img, EdgeDetectionType.CENTER_EIGHT)
    # edgeDetection.apply_filter()
    # edgeDetection.display_filtered()

    # new values for pixel at (0, 0)
    # radius 1: (138, 159, 192)
    # radius 2: (137, 159, 191)
    # radius 3: (137, 158, 191)
    # radius 4: (137, 158, 191)
    # radius 5: (137, 158, 191)
    # radius 6: (136, 159, 191)
    # radius 7: (137, 159, 191)

    # todo same issue here of image darkening not sure due to what
    # gaussianBlur = GaussianBlur(img, 1)
    # gaussianBlur.apply_filter()
    # gaussianBlur.display_filtered()

    # sharpen = Sharpen(img)
    # sharpen.apply_filter()
    # sharpen.display_filtered()

if __name__ == "__main__":
    main()
