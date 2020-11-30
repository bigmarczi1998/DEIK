import math

maxim = -math.inf
minim = math.inf

s = [21, 4, -3, 23, 45, -21]

for item in s:
    if item > maxim:
        maxim = item
    if item < minim:
        minim = item

print(maxim, minim)
