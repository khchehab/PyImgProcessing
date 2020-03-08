import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as t
import math
import time

def main():
    print("Determine the best option to hold the kernels and calculate if based on formula")

    radiuses = [i for i in range(21)]

    with_numpy_times = [gk_with_numpy(radius, (2 * radius) + 1, ((2 * radius) + 1) / 2) for radius in radiuses]
    without_numpy_times = [gk_without_numpy(radius, (2 * radius) + 1, ((2 * radius) + 1) / 2) for radius in radiuses]
    with_some_numpy_times = [gk_with_some_numpy(radius, (2 * radius) + 1, ((2 * radius) + 1) / 2) for radius in radiuses]
    without_numpy2_times = [gk_without_numpy_2(radius, (2 * radius) + 1, ((2 * radius) + 1) / 2) for radius in radiuses]
    with_some_numpy2_times = [gk_with_some_numpy_2(radius, (2 * radius) + 1, ((2 * radius) + 1) / 2) for radius in radiuses]

    plt.ylabel('Kernel Radius')
    plt.xlabel('Time (in nanoseconds)')
    plt.yticks(np.arange(0, len(radiuses), step=5))
    plt.gca().get_xaxis().set_major_formatter(t.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.plot(with_numpy_times, radiuses, label="With numpy")
    plt.plot(without_numpy_times, radiuses, label="Without numpy")
    plt.plot(with_some_numpy_times, radiuses, label="Some numpy")
    plt.plot(without_numpy2_times, radiuses, label="Without numpy 2")
    plt.plot(with_some_numpy2_times, radiuses, label="Some numpy 2")
    plt.legend()
    plt.show()

# this is the best option
def gk_with_numpy(radius, length, sigma):
    start = time.time_ns()
    gaussian_kernel = np.fromfunction(lambda x, y: g(-radius + x, -radius + y, sigma), (length, length))
    gaussian_kernel /= np.sum(gaussian_kernel)
    end = time.time_ns()
    return end - start

def gk_without_numpy(radius, length, sigma):
    start = time.time_ns()
    gaussian_kernel = list(list(g(-radius + x, -radius + y, sigma)
                                for x in range(length))
                           for y in range(length))

    kernel_sum = math.fsum(math.fsum(r) for r in gaussian_kernel)

    for x in range(length):
        for y in range(length):
            gaussian_kernel[x][y] = gaussian_kernel[x][y] / kernel_sum

    x = np.array(gaussian_kernel)
    end = time.time_ns()
    return end - start

def gk_with_some_numpy(radius, length, sigma):
    start = time.time_ns()
    gaussian_kernel = list(list(g(-radius + x, -radius + y, sigma)
                                for x in range(length))
                           for y in range(length))

    x = np.array(gaussian_kernel)
    x /= np.sum(x)
    end = time.time_ns()
    return end - start

def gk_without_numpy_2(radius, length, sigma):
    start = time.time_ns()
    kernel_sum = 0

    gaussian_kernel = [[None for i in range(length)] for j in range(length)]
    for x in range(length):
        for y in range(length):
            kernel_value = g(-radius + x, -radius + y, sigma)
            gaussian_kernel[x][y] = kernel_value
            kernel_sum += kernel_value

    for x in range(length):
        for y in range(length):
            gaussian_kernel[x][y] = gaussian_kernel[x][y] / kernel_sum

    x = np.array(gaussian_kernel)
    end = time.time_ns()
    return end - start

def gk_with_some_numpy_2(radius, length, sigma):
    start = time.time_ns()
    kernel_sum = 0

    gaussian_kernel = [[None for i in range(length)] for j in range(length)]
    for x in range(length):
        for y in range(length):
            kernel_value = g(-radius + x, -radius + y, sigma)
            gaussian_kernel[x][y] = kernel_value
            kernel_sum += kernel_value

    x = np.array(gaussian_kernel)
    x /= kernel_sum
    end = time.time_ns()
    return end - start

def g(x, y,sigma):
    return 1 / (2 * math.pi * sigma * sigma) * (math.e ** (-((x * x) + (y * y)) / (2 * sigma * sigma)))

if __name__ == "__main__":
    main()
