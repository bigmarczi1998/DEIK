import numpy as np


def is_sorted(v):
    idx = int(input('Index: '))

    for i in range(idx - 1):  # index -1es tagjaig nezi
        for j in range(i + 1, idx):  # elso elemtol indexig
            if v[j] < v[i]:  # ha az elotte levo elem kisebb akkor cserel
                v[i], v[j] = v[j], v[i]

    for i in range(idx, v.size - 1):
        for j in range(i + 1, v.size):
            if v[j] > v[i]:
                v[i], v[j] = v[j], v[i]

    print(v)


v = np.random.randint(1, 15, size=20)
print(v)
is_sorted(v)
