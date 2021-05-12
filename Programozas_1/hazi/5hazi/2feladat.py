import numpy as np


def avg_m(m):
    avg_all = m.mean()
    print('matrix atlag: ', avg_all)
    avg_oszlop = m.mean(0)
    print('oszlop atlag: ', avg_oszlop)

    for i in range(m.shape[0]):
        if avg_all < avg_oszlop[i]:
            for j in range(m.shape[1]):
                m.astype(float)
                m[j, i] = (m[j, i]) / 2

    print(m)


meret = input("Mátrix mérete: ")
sor, oszlop = meret.split()
m = np.random.randint(0, 100, (int(sor), int(oszlop)))
print('matrix\n', m)

avg_m(m.astype(np.float))
