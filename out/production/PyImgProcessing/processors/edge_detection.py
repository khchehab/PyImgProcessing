from processors.kernel_operation import KernelOperation
from model.kernel import Kernel
from enum import Enum

# todo maybe add more edge detection types
#      check canny edge detection, etc...

class EdgeDetectionType(Enum):
    CENTER_ZERO = [[1,  0, -1],
                   [0,  0,  0],
                   [-1, 0,  1]]
    CENTER_FOUR = [[0,  1, 0],
                   [1, -4, 1],
                   [0,  1, 0]]
    CENTER_EIGHT = [[-1, -1, -1],
                    [-1,  8, -1],
                    [-1, -1, -1]]

class EdgeDetection(KernelOperation):
    def __init__(self, filename, edge_detection_type = EdgeDetectionType.CENTER_ZERO):
        super(EdgeDetection, self).__init__(filename, 1)
        self.__edge_detection_type = edge_detection_type

    def _get_kernel(self):
        return Kernel(self._kernel_length, self.__edge_detection_type.value)