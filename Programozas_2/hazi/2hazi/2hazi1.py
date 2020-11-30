class Matrix:

    def __init__(self, sor, oszlop, matrix):
        self.n = sor
        self.m = oszlop
        self.mtx = matrix

    def transposes(self):
        import numpy as np
        mtx2 = np.zeros((self.n, self.m), dtype='int')
        for i in range(self.n):
            for k in range(self.m):
                mtx2[i][k] = self.mtx[k][i]
        return mtx2

    def get_odd_sum(self):
        odd = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.mtx[i, j] % 2 == 1:
                    odd += self.mtx[i, j]
        return odd

    def is_equal_columnsum(self):
        import math
        new_list = []
        a = list(zip(*self.mtx))
        for k in range(len(a)):
            new_list.append(a[k])
        res = {idx + 1: new_list[idx] for idx in range(len(new_list))}
        sz = -math.inf
        hely = 0
        for k, v in res.items():
            if sum(v) == sz:
                hely_2 = "{{{0}: {1}}}".format(k, v)
                return '{}\n{}\nosszeg: {}'.format(hely, hely_2, sum(v))
            else:
                sz = sum(v)
                hely = ("{{{0}: {1}}}".format(k, v))

    def __str__(self):
        return 'Mátrix:\n{}\nTranszponáltja:\n{}\nPáratlan számok összege:\n{}\nEgyenlő összegű oszlopok:\n{}'.format(
            self.mtx, self.transposes(), self.get_odd_sum(), self.is_equal_columnsum())


import numpy as np1

mtx3 = np1.random.randint(0, 10, (3, 3), dtype='int')
m1 = Matrix(3, 3, mtx3)
print(m1.__str__())
