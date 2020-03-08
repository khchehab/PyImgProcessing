import time
import math

NUMBER_OF_EXECUTIONS = 1

def main():
    radius = 5
    length = (2 * radius) + 1
    sigma = length / 2

    m1 = avg_f(f1, radius, length, sigma)
    m2 = avg_f(f2, radius, length, sigma)
    diff = abs(m1 - m2)

    print("Method #1 (One Liners) - Average elapsed: %s nanoseconds" % (f'{m1:,}'))
    print("Method #2 (Explicit Loop) - Average elapsed: %s nanoseconds" % (f'{m2:,}'))
    print("Difference between methods 1 and 2 - %s nanoseconds" % (f'{diff:,}'))

def f2(r, l, s):
    gaussian_kernel = [[None for i in range(l)] for j in range(l)]
    weighted_sum = 0

    i = 0
    for x in range(-r, r + 1):
        j = 0
        for y in range(-r, r + 1):
            gaussian_value = g(x, y, s)
            weighted_sum += gaussian_value
            gaussian_kernel[i][j] = gaussian_value
            j += 1
        i += 1

    for x in range(l):
        for y in range(l):
            gaussian_kernel[x][y] = gaussian_kernel[x][y] / weighted_sum

def avg_f(f, r, l, s):
    elapsed = 0

    for i in range(NUMBER_OF_EXECUTIONS):
        start = time.time_ns()
        f(r, l, s)
        end = time.time_ns()

        elapsed += end - start

    return elapsed / NUMBER_OF_EXECUTIONS

def f1(r, l, s):
    k = list(list(g(-r + x, -r + y, s) for x in range(l)) for y in range(l))
    sumk = math.fsum(math.fsum(v) for v in k)

    # with this the difference was in the range of ]0,1.] ns
    for x in range(l):
        for y in range(l):
            k[x][y] = k[x][y] / sumk

    # with this the difference was in the range of [3,5] ns
    # k = list(list(k[x][y] / sumk for x in range(l)) for y in range(l))

def g(x, y, sigma):
    return 1 / (2 * math.pi * sigma * sigma) * math.exp(-((x * x) + (y * y)) / (2 * sigma * sigma))

if __name__ == "__main__":
    main()
