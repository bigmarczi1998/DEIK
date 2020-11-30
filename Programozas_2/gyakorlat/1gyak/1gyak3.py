import numpy as np

sor = int(input("Kerem a sorok szamat: "))
oszlop = int(input('Kerem az oszlopok szamat: '))

mtx = np.zeros((sor, oszlop))

for i in range(sor):
    for j in range(oszlop):
        mtx[i, j] = i * j

print(mtx)
