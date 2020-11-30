#np.fuggvenyeink
#np.arange
#np.zeros_like(a)


# #1
# import numpy as np
#
# def vektor_fordit(a):
#     b=np.zeros_like(a)
#     for i in range(a.size):
#         b[i]=a[a.size-i-1]
#     print('A: {}'.format(a))
#     print('B: {}'.format(b))
#
# a=np.arange(10,50)
# vektor_fordit(a)

#2
#tobb feltetelel keresni numpyba
# import numpy as np
#
# b=np.random.randint(1,50,size=10)
# min_max_values = b[(b == b.min()) | (b == b.max())]
# print(b)
# print(min_max_values)
# min_max_indices = np.where((b == b.min()) | (b == b.max())) #np.where fuggveny
# print(min_max_indices)

#3
# import numpy as np
# c=np.random.randint(1,100,size=30)
# print(c)
# print(c.max())
# c[c==c.max()]=-1 #maxot megkeresi es felulirja
# print(c)

#4
#random vektor rendezese
# import numpy as np
#
# def vektor_rendezo(d):
#     for i in range(d.size -1):
#         for j in range(i+1,d.size):
#             if d[i]>d[j]: #aktualis nagyobb mit a masik, akkor nincsen jol rendezve
#                 d[i],d[j]=d[j],d[i]
#     return d
#
# d=np.random.randint(1,100,size=30) #deklaralok egy random vektort
# print(d)
# sorted=vektor_rendezo(d)
# print(sorted)

#5
# import numpy as np
#
# e=np.arange(-5,15)
# print(e)
# e[(e>3) & (e<8)]*=-1
# print(e)

#6
# import numpy as np
#
# f=np.random.randint(1,50,size=10)
# print(f)
# num=int(input('Kerek egy szamot:'))
#
# dist=np.abs(num - f) #parameter a -f tavolsag
# print(dist)
#
# min_helyek=np.where(dist==dist.min())
# print(f[min_helyek])

#7
# import numpy as np
#
# g=np.random.randint(-50,50,size=30)
# print(g)
#
# pos=g[g>0]
# print('pozitiv szamok:',pos)
# neg=g[g<0]
# print('negativ szamok:',neg)
# zeros=g[g==0]
# print('zero szamok:',zeros)
#
# print('pozitiv: {}, negativ: {}, nullak: {}'.format(pos.size,neg.size,zeros.size))