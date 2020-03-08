from processors.kernel_operation import KernelOperation
from model.kernel import Kernel

class Sharpen(KernelOperation):
    def __init__(self, filename):
        super(Sharpen, self).__init__(filename, 1)

    def _get_kernel(self):
        return Kernel(self._kernel_length, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
