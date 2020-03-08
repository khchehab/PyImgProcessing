from processing.image_operation import ImageOperation
import numpy as np

# This file will contain all image operations (such as converting an image to grayscale)

class Grayscale(ImageOperation):
    def __init__(self, filename):
        super(Grayscale, self).__init__(filename=filename, filtered_mode='L', filtered_cmap='gray')

    def apply_operation(self):
        img_pixels = self._get_original_pixels()

        # todo allow later on to get grayscale value based on different methods
        grayscale_func = self.__get_average_grayscale

        # todo see if the below for loop can be replaced with np.fromfunction call
        filtered_pixels = np.zeros((img_pixels.shape[0], 1), dtype=np.uint8)
        for i in range(len(img_pixels)):
            filtered_pixels[i] = grayscale_func(img_pixels[i])

        self._set_filtered(filtered_pixels)

    def __get_average_grayscale(self, pixel):
        return pixel.mean()