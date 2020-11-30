import numpy as np
number=np.random.randint(1,10,size=10)
print(number)
avg=np.average(number)
print('Átlag:',avg)
dist=np.abs(avg-number)
print(dist)