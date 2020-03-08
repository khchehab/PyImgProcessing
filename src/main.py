from processing.image_operations import Grayscale
from processing.kernel_operations import Identity, Sharpen, GaussianBlur

def main():
    img = "../res/valve.png"

    gaussianBlur = Grayscale(filename=img)
    gaussianBlur.apply_operation()
    gaussianBlur.display()

    # import numpy as np
    # from PIL import Image
    # import matplotlib.pyplot as plt
    #
    # a = np.random.randint(255, size=(28*28))
    # img = Image.fromarray(a.reshape(28,28), 'L')
    # plt.imshow(img, cmap='gray')
    # plt.show()

if __name__ == "__main__":
    main()
