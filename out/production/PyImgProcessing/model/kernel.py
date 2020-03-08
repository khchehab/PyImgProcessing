class Kernel:
    def __init__(self, length, matrix=None):
        if length < 0:
            raise ValueError("Kernel length should be a positive number")
        if matrix is not None and len(matrix) != length:
            raise ValueError("The matrix should have the same specified length")

        self.length = length

        if matrix is None:
            matrix = [[None for i in range(length)] for j in range(length)]

        self.__matrix = matrix

    def set_value(self, i, j, value):
        if i < 0 or i >= self.length:
            raise ValueError("i is out of bounds")
        if j < 0 or j >= self.length:
            raise ValueError("j is out of bounds")
        self.__matrix[i][j] = value

    def get_value(self, i, j):
        if i < 0 or i >= self.length:
            raise ValueError("i is out of bounds")
        if j < 0 or j >= self.length:
            raise ValueError("j is out of bounds")
        return self.__matrix[i][j]

    def print(self):
        print(*self.__matrix, sep="\n")
