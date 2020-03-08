from processors.kernel_operation import KernelOperation
from model.kernel import Kernel

class Identity(KernelOperation):
    def __init__(self, filename):
        super(Identity, self).__init__(filename, 1)

    def _get_kernel(self):
        return Kernel(self._kernel_length, [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
