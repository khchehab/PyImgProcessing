# todo check if this can be integrated into one of the files image_operations or kernel_operations in order not to have it in its own file alone

from processing.image_operation import ImageOperation
from processing.image_operations import Grayscale
from processing.kernel_operations import GaussianBlur
import numpy as np

class CannyEdgeDetection(ImageOperation):
    def __init__(self, filename):
        super(CannyEdgeDetection, self).__init__(filename=filename)

    def apply_operation(self):
        # step 0: convert the image to grayscale
        grayscale = Grayscale(filename=self._ImageOperation__filename)
        grayscale.apply_operation()
        grayscale_pixels = np.array(grayscale._ImageOperation__filtered.getdata())

        mode = grayscale._ImageOperation__filtered_mode
        size = grayscale._ImageOperation__original_size

        print(grayscale_pixels)
        print(grayscale_pixels.shape)
        print(grayscale_pixels.reshape(size))
        print(grayscale_pixels.reshape(size).shape)
        print(mode)
        print(size)

        from PIL import Image
        import matplotlib.pyplot as plt
        grayscale_img = Image.frombuffer(mode, size, grayscale_pixels)
        plt.imshow(grayscale._ImageOperation__filtered, cmap='gray')
        plt.show()

        # step 1: gaussian blur with 5x5 kernel
        # gaussian_blur = GaussianBlur(image_pixels=grayscale_pixels, blur_radius=2, image_mode=mode, image_size=size)
        # gaussian_blur.apply_operation()
        # gaussian_blur.display()

        # step 2: find magnitude and gradient orientation


        # step 3: apply non-maximum suppression
        # step 4: apply hysteresis threshold

def main():
    img = "../../res/valve.png"
    edge = CannyEdgeDetection(img)
    edge.apply_operation()

if __name__ == "__main__":
    main()
