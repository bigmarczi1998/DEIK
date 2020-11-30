import numpy as np


def szimmetrikus_matrix(mtx, n):
    for i in range(n):
        for j in range(i):
            if mtx[i, j] != mtx[j, i]:
                return 'Hamis, nem szimmetrikus!'
    return 'Igaz, ez egy szimmetrikus matrix.'


n = int(input('n= '))
mtx = np.zeros((n, n), dtype='int')
for a in range(n):
    for b in range(n):
        mtx[a, b] = int(input('szam hozzaadasa a matrixhoz: '))  # sor szerint olvas be


print('Matrix:\n' , mtx)
print('Matrix transzponaltja:\n', mtx.transpose())
print(szimmetrikus_matrix(mtx, n))
