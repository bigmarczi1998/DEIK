import numpy as np
def reader(a,b,c):
    number=np.random.randint(int(a),int(b),size=int(c))
    print('Vektor:',number)

    avg=np.average(number)
    print('Átlag',avg)

    elem=[]
    hely=[]

    for i in range(number.size):
        if (number[i]<avg) and (number[i]%2==0):
            elem.append(number[i])
            hely.append(i)

    print('Elemek:',elem)
    print('Helyeik:',hely)

number=str(input('Szamok: '))
a,b,c=number.split()
reader(a,b,c)