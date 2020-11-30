import numpy as np

n = int(input('Matrix merete: '))
mtx = np.random.randint(1, 10, (n, n), dtype='int')

print(mtx, '\n', mtx.transpose())
