from abc import abstractmethod
from processing.image_operation import ImageOperation
import numpy as np

class KernelOperation(ImageOperation):
    def __init__(self, filename=None, filtered_mode=None, filtered_cmap=None, kernel_radius=1, is_separable=False):
        super(KernelOperation, self).__init__(filename=filename, filtered_mode=filtered_mode,
                                              filtered_cmap=filtered_cmap)

        if kernel_radius < 0:
            raise ValueError('Kernel radius cannot be a negative number')

        self.__kernel_radius = kernel_radius
        self.__kernel_length = (2 * kernel_radius) + 1
        self.__is_separable = is_separable

    @abstractmethod
    def _get_kernel(self):
        pass

    def apply_operation(self):
        kernel = self._get_kernel()
        width, height = self._ImageOperation__original.size
        channel = 3 # todo check if 3 here can be parameterized
        filtered_shape = (width * height, channel)
        img_pixels = self._get_original_pixels()
        filtered_pixels = self.__apply_separable_filter(kernel, width, height, img_pixels, filtered_shape) if self.__is_separable\
                          else self.__apply_non_separable_filter(kernel, width, height, img_pixels, filtered_shape, channel)
        filtered_pixels = filtered_pixels.astype('uint8')
        self._set_filtered(filtered_pixels)

    def __apply_separable_filter(self, kernel, width, height, img_pixels, filtered_shape):
        filtered_pixels = np.zeros(filtered_shape)
        filtered_pixels_i = np.zeros(filtered_shape)

        # horizontal
        for i in range(width):
            for j in range(height):
                for ki in range(self.__kernel_length):
                    myi = i + ki - self.__kernel_radius
                    myi = myi if 0 <= myi < width else 0 if myi < 0 else width - 1

                    filtered_pixels_i[self.__index(i, j, width)] += img_pixels[self.__index(myi, j, width)] *\
                                                                    kernel[ki]

        # vertical
        for i in range(width):
            for j in range(height):
                for kj in range(self.__kernel_length):
                    myj = j + kj - self.__kernel_radius
                    myj = myj if 0 <= myj < height else 0 if myj < 0 else height - 1

                    filtered_pixels[self.__index(i, j, width)] += filtered_pixels_i[self.__index(i, myj, width)] *\
                                                                  kernel[kj]

        return filtered_pixels

    def __apply_non_separable_filter(self, kernel, width, height, img_pixels, filtered_shape, channel):
        filtered_pixels = np.zeros(filtered_shape)

        for i in range(width):
            for j in range(height):
                for ki in range(self.__kernel_length):
                    for kj in range(self.__kernel_length):
                        myi = i + ki - self.__kernel_radius
                        myi = myi if 0 <= myi < width else 0 if myi < 0 else width - 1

                        myj = j + kj - self.__kernel_radius
                        myj = myj if 0 <= myj < height else 0 if myj < 0 else height - 1

                        filtered_pixels[self.__index(i, j, width)] += img_pixels[self.__index(myi, myj, width)] *\
                                                                      kernel[ki, kj]

        return filtered_pixels.clip(min=np.zeros(channel), max=np.full(3, 255, dtype=np.uint8))

    def __index(self, i, j, width):
        return (j * width) + i
