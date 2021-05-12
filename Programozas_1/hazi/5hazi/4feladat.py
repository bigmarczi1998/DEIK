import numpy as np


def matrix_szorzat(v, mtx):
    for i in range(v.size):
        for j in range(m):
            mtx[i, j] *= v[i]
    return mtx


while True:
    try:
        vektor = int(input("vektor meret: "))
        v = np.random.randint(1, 10, size=vektor)
        print('vektor:', v)

        n = int(input('matrix sor= '))
        if vektor == n:

            m = int(input('matrix oszlop= '))
            mtx = np.zeros((n, m), dtype='int')
            for a in range(n):
                for b in range(m):
                    mtx[a, b] = int(input('szam hozzaadasa a matrixhoz: '))  # sor szerint olvas be

            print('Matrix:\n', mtx)

            print("Matrix szorzasa vektorral:\n", matrix_szorzat(v, mtx))
            break

        else:
            raise Exception('Nem megoldhato, mert vektor meret != mtx sorral.')

    except Exception as e:
        print(e)
        break
