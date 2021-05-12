import numpy as np
number=np.arange(1,300,3)
print(number)
db=0
for i in range(number.size):
    if (number[i])%(4)==0:
        number[i]=-4
        db+=1
print(db)