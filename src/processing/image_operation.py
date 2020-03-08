from abc import ABC, abstractmethod
from os.path import exists
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class ImageOperation(ABC):
    def __init__(self, filename=None, filtered_mode=None, filtered_cmap=None):
        if filename is None:
            raise ValueError("The file name should not be empty")
        if not exists(filename):
            raise ValueError("The file %s does not exist" % (filename, ))

        self.__original = Image.open(filename)
        self.__original_pixels = np.array(self.__original.getdata())
        self.__filename = filename
        self.__filtered = None
        self.__filtered_cmap = filtered_cmap
        self.__filtered_mode = self.__original.mode if filtered_mode is None else filtered_mode

    @abstractmethod
    def apply_operation(self):
        pass

    def display(self):
        ncols = 1 if self.__filtered is None else 2

        _, plts = plt.subplots(ncols=ncols, squeeze=False)
        plts[0,0].imshow(self.__original)
        plts[0,0].tick_params(which='both', top=False, right=False, bottom=False, left=False, labeltop=False,
                              labelright=False, labelbottom=False, labelleft=False)

        if ncols == 1:
            print("No operation has been applied to the image, only the original is displayed")
        else:
            plts[0,1].imshow(self.__filtered, self.__filtered_cmap)
            plts[0,1].tick_params(which='both', top=False, right=False, bottom=False, left=False, labeltop=False,
                                  labelright=False, labelbottom=False, labelleft=False)

        plt.show()

    def _get_original_pixels(self):
        return self.__original_pixels

    def _set_filtered(self, filtered_pixels):
        self.__filtered = Image.frombuffer(self.__filtered_mode, self.__original.size, filtered_pixels)
