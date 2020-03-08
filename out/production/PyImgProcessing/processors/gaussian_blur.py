from processors.kernel_operation import KernelOperation
from model.kernel import Kernel
import math

class GaussianBlur(KernelOperation):
    def __init__(self, filename, blur_radius):
        super(GaussianBlur, self).__init__(filename, blur_radius)
        self.__sigma = self._kernel_length / 2

    def _get_kernel(self):
        gaussian_kernel = list(list(self.__get_gaussian_value(-self._kernel_radius + x, -self._kernel_radius + y)
                                    for x in range(self._kernel_length))
                               for y in range(self._kernel_length))

        kernel_sum = math.fsum(math.fsum(r) for r in gaussian_kernel)

        for x in range(self._kernel_length):
            for y in range(self._kernel_length):
                gaussian_kernel[x][y] = gaussian_kernel[x][y] / kernel_sum

        return Kernel(self._kernel_length, gaussian_kernel)

    # x is the distance from the center to the horizontal axis
    # y is the distance from the center to the vertical axis
    def __get_gaussian_value(self, x, y):
        return 1 / (2 * math.pi * self.__sigma * self.__sigma) * math.exp(-((x * x) + (y * y)) / (2 * self.__sigma * self.__sigma))
