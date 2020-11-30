import numpy as np


class Matrix:
    def __init__(self, sor, oszlop):
        self.n = sor
        self.m = oszlop
        self.mtx = np.zeros((self.n, self.m))

    def feltolt(self):
        for i in range(self.n):
            for j in range(self.m):
                self.mtx[i, j] = i * j
        print(self.mtx)


m1 = Matrix(3, 4)
m2 = Matrix(2, 5)
m3 = Matrix(12, 12)

m3.feltolt()