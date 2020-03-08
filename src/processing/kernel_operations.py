from processing.kernel_operation import KernelOperation
import numpy as np
import math

class Identity(KernelOperation):
    def __init__(self, filename):
        super(Identity, self).__init__(filename=filename, kernel_radius=1)

    def _get_kernel(self):
        return np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

class Sharpen(KernelOperation):
    def __init__(self, filename):
        super(Sharpen, self).__init__(filename=filename, kernel_radius=1)

    def _get_kernel(self):
        return np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

class GaussianBlur(KernelOperation):
    def __init__(self, filename, blur_radius):
        super(GaussianBlur, self).__init__(filename=filename, kernel_radius=blur_radius, is_separable=True)
        self.__sigma = self._KernelOperation__kernel_length / 2

    def _get_kernel(self):
        # get a 1d gaussian kernel since gaussian kernels are separable
        kernel = np.fromfunction(lambda x: self.__gaussian_value(-self._KernelOperation__kernel_radius + x),
                                 (self._KernelOperation__kernel_length,))
        # normalize the kernel
        return kernel / np.sum(kernel)

    # get the gaussian value as a 1d kernel
    def __gaussian_value(self, x):
        return 1 / (2 * math.pi * self.__sigma * self.__sigma) * (math.e ** (-(x * x) / (2 * self.__sigma * self.__sigma)))
