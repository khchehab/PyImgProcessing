from PIL import Image, ImageFilter
from PIL.ImageFilter import Kernel
import math
import time
import numpy as np

def main():
    im = Image.open("../res/TajMahal.jpeg")
    print("First pixel's value:")
    print(im.getpixel((0, 0)))
    print()

    r = 1

    start = time.time_ns()
    correct_im = im.filter(ImageFilter.GaussianBlur(r))
    end = time.time_ns()
    elapsed = end - start
    print("Pillow's gaussian blur took %s nanoseconds" % (f'{elapsed:,}'))

    print("First pixel's value of the blurred image:")
    print(correct_im.getpixel((0, 0)))
    print()

    my_im = Image.new(im.mode, im.size)
    my_img = my_im.load()

    start = time.time_ns()
    kernel = gk(r)
    end = time.time_ns()
    elapsed = end - start
    print("creating the gaussian kernel took %s nanoseconds" % (f'{elapsed:,}'))

    print(*kernel, sep="\n")

    # try to see why when i wrote this it works but not my original code
    # whats the difference?????
    start = time.time_ns()
    # for i in range(im.width - 1, -1, -1):
    #     for j in range(im.height - 1, -1, -1):
    #         accum = (0, 0, 0)
    #
    #         for ki in range(len(kernel) - 1, -1, -1):
    #             for kj in range(len(kernel) - 1, -1, -1):
    #                 myi = i + ki - r
    #                 myj = j + kj - r
    #
    #                 rr = im.getpixel((
    #                     0 if myi < 0 else im.width - 1 if myi > im.width - 1 else myi,
    #                     0 if myj < 0 else im.height - 1 if myj > im.height - 1 else myj
    #                 ))
    #                 rrr = tuple(kernel[ki][kj] * p for p in rr)
    #                 accum = tuple(math.fsum(p) for p in zip(accum, rrr))
    #
    #         my_img[i, j] = tuple(int(kkk) for kkk in accum)

    # for i in range(im.width):
    #     for j in range(im.height):
    #         accum = (0, 0, 0)
    #
    #         for ki in range(len(kernel)):
    #             for kj in range(len(kernel)):
    #                 myi = i + ki - r
    #                 myj = j + kj - r
    #
    #                 rr = im.getpixel((
    #                     0 if myi < 0 else im.width - 1 if myi > im.width - 1 else myi,
    #                     0 if myj < 0 else im.height - 1 if myj > im.height - 1 else myj
    #                 ))
    #                 rrr = tuple(kernel[ki][kj] * p for p in rr)
    #                 accum = tuple(math.fsum(p) for p in zip(accum, rrr))
    #
    #         my_img[i, j] = tuple(int(kkk) for kkk in accum)

    # convolve horizontally

    # convole vertically

    end = time.time_ns()
    elapsed = end - start
    print("convolving the image took %s nanoseconds" % (f'{elapsed:,}'))

    print("First pixel's value of my blurred image:")
    print(my_im.getpixel((0, 0)))
    print()

    my_im.show()

def gk(r):
    l = (2 * r) + 1
    sigma = l / 2
    gaussian_kernel = list(list(g(-r + x, -r + y, sigma)
                                for x in range(l))
                           for y in range(l))

    kernel_sum = math.fsum(math.fsum(r) for r in gaussian_kernel)

    print(kernel_sum)

    for x in range(l):
        for y in range(l):
            gaussian_kernel[x][y] = gaussian_kernel[x][y] / kernel_sum

    return gaussian_kernel

def g(x, y,sigma):
    return 1 / (2 * math.pi * sigma * sigma) * math.exp(-((x * x) + (y * y)) / (2 * sigma * sigma))

    # new values for pixel at (0, 0)
    # radius 1: (138, 159, 192)
    # radius 2: (137, 159, 191)
    # radius 3: (137, 158, 191)
    # radius 4: (137, 158, 191)
    # radius 5: (137, 158, 191)
    # radius 6: (136, 159, 191)
    # radius 7: (137, 159, 191)


if __name__ == "__main__":
    main()