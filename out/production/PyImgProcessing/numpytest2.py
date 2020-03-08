from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as t
import math
import time

def main():
    print("Determine the best way to convole an image with a kernel")

    img = Image.open("../res/TajMahal.jpeg")
    img_pixels = np.array(img.getdata())

    radius = 1
    kernel = gaussian_kernel(radius)

    # blurred = gaussian_blur_1(radius, img, kernel)
    # blurred.show()

    # blurred_img = Image.new(img.mode, img.size)
    # gaussian_blur_2(radius, img.width, img.height, img_pixels, kernel, blurred_img.load())
    # blurred_img.show()

    # blurred_pixels = gaussian_blur_3(radius, img.width, img.height, img_pixels, kernel)
    # blurred_img = Image.frombuffer(img.mode, img.size, blurred_pixels)
    # blurred_img.show()

    blurred_pixels = gaussian_blur_4(radius, img.width, img.height, img_pixels, kernel)
    blurred_img = Image.frombuffer(img.mode, img.size, blurred_pixels)
    blurred_img.show()

# new values for pixel at (0, 0)
# without anything: (139, 159, 192)
# radius 1: (138, 159, 192)
# radius 2: (137, 159, 191)
# radius 3: (137, 158, 191)
# radius 4: (137, 158, 191)
# radius 5: (137, 158, 191)
# radius 6: (136, 159, 191)
# radius 7: (137, 159, 191)

def gaussian_blur_4(radius, width, height, img_pixels, kernel):
    blurred_pixels = np.zeros((width * height, 3), dtype=np.float64)

    for i in range(width):
        for j in range(height):
            for ki in range(len(kernel)):
                for kj in range(len(kernel)):
                    myi = i + ki - radius
                    myi = myi if 0 <= myi < width else 0 if myi < 0 else width - 1

                    myj = j + kj - radius
                    myj = myj if 0 <= myj < height else 0 if myj < 0 else height - 1

                    blurred_pixels[(j * width) + i] = np.add(blurred_pixels[(j * width) + i], img_pixels[(myj * width) + myi] * kernel[ki, kj], casting='safe')

    blurred_pixels = blurred_pixels.astype('uint8')
    print(blurred_pixels[0])
    return blurred_pixels

def gaussian_blur_3(radius, width, height, img_pixels, kernel):
    blurred_pixels = np.empty((width * height, 3), dtype=np.uint8)

    for i in range(width):
        for j in range(height):
            accum = (0, 0, 0)

            for ki in range(len(kernel)):
                for kj in range(len(kernel)):
                    myi = i + ki - radius
                    myi = myi if 0 <= myi < width else 0 if myi < 0 else width - 1

                    myj = j + kj - radius
                    myj = myj if 0 <= myj < height else 0 if myj < 0 else height - 1

                    pixel = img_pixels[(myj * width) + myi]
                    pixel_multiplied = tuple(kernel[ki, kj] * p for p in pixel)
                    accum = tuple(math.fsum(p) for p in zip(accum, pixel_multiplied))

            blurred_pixels[(j * width) + i] = tuple(int(p) for p in accum)

    print(blurred_pixels[0])
    return blurred_pixels

def gaussian_blur_2(radius, width, height, img_pixels, kernel, blurred_pixels):
    for i in range(width):
        for j in range(height):
            accum = (0, 0, 0)

            for ki in range(len(kernel)):
                for kj in range(len(kernel)):
                    myi = i + ki - radius
                    myi = myi if 0 <= myi < width else 0 if myi < 0 else width - 1

                    myj = j + kj - radius
                    myj = myj if 0 <= myj < height else 0 if myj < 0 else height - 1

                    pixel = img_pixels[(myj * width) + myi]
                    pixel_multiplied = tuple(kernel[ki, kj] * p for p in pixel)
                    accum = tuple(math.fsum(p) for p in zip(accum, pixel_multiplied))

            blurred_pixels[i, j] = tuple(int(p) for p in accum)

    print(blurred_pixels[0, 0])

def gaussian_blur_1(radius, img, kernel):
    blurred_img = Image.new(img.mode, img.size)
    blurred = blurred_img.load()

    for i in range(img.width):
        for j in range(img.height):
            accum = (0, 0, 0)

            for ki in range(len(kernel)):
                for kj in range(len(kernel)):
                    myi = i + ki - radius
                    myi = myi if 0 <= myi < img.width else 0 if myi < 0 else img.width - 1

                    myj = j + kj - radius
                    myj = myj if 0 <= myj < img.height else 0 if myj < 0 else img.height - 1

                    pixel = img.getpixel((myi, myj))
                    pixel_multiplied = tuple(kernel[ki, kj] * p for p in pixel)
                    accum = tuple(math.fsum(p) for p in zip(accum, pixel_multiplied))

            blurred[i, j] = tuple(int(p) for p in accum)

    print(blurred[0, 0])
    return blurred_img

def gaussian_kernel(radius):
    length = (2 * radius) + 1
    sigma = length / 2
    kernel = np.fromfunction(lambda x, y: gaussian_value(-radius + x, -radius + y, sigma), (length, length))
    return kernel / np.sum(kernel)

def gaussian_value(x, y,sigma):
    return 1 / (2 * math.pi * sigma * sigma) * (math.e ** (-((x * x) + (y * y)) / (2 * sigma * sigma)))

if __name__ == "__main__":
    main()
