import numpy as np
number=np.random.randint(1,90,size=5)
print(number)
while True:
    try:
        input_number=int(input())
        if input_number in number :
            print('Találat!')
            break
        else:
            raise Exception('Nem talált!')
    except Exception as e:
        print(e)