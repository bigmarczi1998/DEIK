from copy import deepcopy

a = [1, 2, 3, 4, 5]
b = a
a[0] = 5
print(a)
print(b)

print('Deepcopy')

c = [1, 2, 3, 4, 5]
d = deepcopy(c)
d[0] = 5
print(c)
print(d)

from random import shuffle

e = [1, 2, 3, 4, 5]
print(e)

print('Shuffle')

shuffle(e)
print(e)
