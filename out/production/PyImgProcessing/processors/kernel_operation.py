import os.path
from abc import ABC, abstractmethod
from PIL import Image
from model.kernel import Kernel

class KernelOperation(ABC):
    def __init__(self, filename, kernel_radius):
        if not filename:
            raise ValueError("Filename should not be empty")

        if not os.path.exists(filename):
            raise ValueError("The file %s does not exist" % filename)

        if kernel_radius < 0:
            raise ValueError("The kernel radius can not be a negative number")

        self.__filename = filename
        self._kernel_radius = kernel_radius
        self._kernel_length = (2 * kernel_radius) + 1

        self.__original = Image.open(filename)
        self.__filtered = Image.new(self.__original.mode, self.__original.size)

    @abstractmethod
    def _get_kernel(self):
        pass

    def display_filtered(self):
        self.__filtered.show()

    def apply_filter(self):
        kernel = self._get_kernel()
        filtered_pixels = self.__filtered.load()

        kernel.print()
        print()

        print("First pixel's value:")
        print(self.__original.getpixel((0, 0)))
        print()

        print("First pixel's value of the blurred image:")
        print(self.__get_pixel_value(self.__get_image_kernel(0, 0), kernel))
        print()

        print("Getting the image kernel at (0, 0):")
        self.__get_image_kernel(0, 0).print()
        print()

        # print("Kernel:")
        # kernel.print()
        # print()
        # print("Image Kernel:")
        # self.__get_image_kernel(0, 0).print()
        # print()
        # print("New pixel at (0, 0) will be:")
        # print(self.__get_pixel_value(self.__get_image_kernel(0, 0), kernel))

        # for i in range(self.__original.width):
        #     for j in range(self.__original.height):
        #         filtered_pixels[i, j] = self.__get_pixel_value(self.__get_image_kernel(i, j), kernel)

    def __get_pixel_value(self, image_kernel, kernel):
        if image_kernel.length != kernel.length:
            raise ValueError("The 2 kernels have different lengths")

        return tuple(sum(x) for x in zip(*list(map(lambda x: tuple(sum(y) for y in zip(*x)), list(list(tuple(int(x * kernel.get_value(i, j))
                                                                                                             for x in image_kernel.get_value(i, j))
                                                                                                       for i in range(self._kernel_length))
                                                                                                  for j in range(self._kernel_length))))))

    def __get_image_kernel(self, i, j):
        image_kernel = Kernel(self._kernel_length)

        i_kernel = 0
        for x in range(i - self._kernel_radius, i + self._kernel_radius + 1):
            j_kernel = 0

            for y in range(j - self._kernel_radius, j + self._kernel_radius + 1):
                image_kernel.set_value(i_kernel, j_kernel, self.__original.getpixel((
                    0 if x < 0 else self.__original.width - 1 if x > self.__original.width - 1 else x,
                    0 if y < 0 else self.__original.height - 1 if y > self.__original.height - 1 else y
                )))

                j_kernel += 1

            i_kernel += 1

        return image_kernel
