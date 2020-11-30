# 1feladat
# import numpy as np
#
# def is_sorted(a):
#     if a[0] < a[1]:
#         for i in range(1,a.size):
#             if a[i - 1] > a[i]:
#                 return "Hamis"
#         return "Igaz"
#     elif a[0] > a[1]:
#         for i in range(1, a.size):
#             if a[i - 1] < a[i]:
#                 return "Hamis"
#         return "Igaz"
#
# # a = np.arange(1,10)
# a = np.random.randint(1,50,size=10)
# print(is_sorted(a))

# 2feladat
# shape alakot jelol, oszlop es sor [0],[1]
# import numpy as np
#
# def oszlop_rendezo(m,ind):
#     for i in range(m.shape[0] - 1): #utolso elotti sorig megy
#         for j in range(i + 1, m.shape[0]): #azt kovető sor a j
#             if m[i, ind] > m[j, ind]:
#                 m[i,ind], m[j,ind] = m[j,ind], m[i,ind] #2.oszlopindex oszlopat novekvo sorrendben rendezi (0,1,2)
#
# m = np.random.randint(1,50,(4,5))
# print(m.shape[0])
# print(m.shape[1])
# print(m)
# ind = int(input("Kerek egy oszlopindexet:"))
# oszlop_rendezo(m,ind)
# print(m)

# 3feladat
# import numpy as np
#
# def sor_oszlop_osszegek(m):
#     row_sum = m.sum(axis = 0)
#     col_sum = m.sum(axis = 1)
#     tmp = row_sum[0]
#     for i in range(m.shape[0]):
#         if tmp != row_sum[i] or tmp != col_sum[i]:
#             return False
#     return True
#
#
# # m = np.random.randint(1,50,(3,3))
# m = np.ones((3,3))
# print(m)
# print(sor_oszlop_osszegek(m))

# 4feladat
# import numpy as np
#
# def oszthato_indexek(m):
#     list = []
#     for i in range(m.shape[0]):
#         for j in range(m.shape[1]):
#             if m[i,j] % (i + 1) == 0 and m[i,j] % (j + 1) == 0:
#                 list.append((m[i,j],i+1,j+1))
#     return list
#
# m = np.random.randint(1,50,(3,4))
# print(oszthato_indexek(m))

# 5feladat
# import numpy as np
#
#
# def count_negative_and_zeros(m):
#     list = []
#     for j in range(m.shape[1]):
#         zeros = 0
#         negative = 0
#         for i in range(m.shape[0]):
#             if m[i, j] == 0:
#                 zeros += 1
#             elif m[i, j] < 0:
#                 negative += 1
#         if negative >= zeros * 2 and zeros > 0:
#             list.append(j)
#     return list
#
#
# sor = input("Kerem a matrix mereteit: ")
# n, m = sor.split()
#
# m = np.random.randint(-1, 1, (int(n), int(m)))
# print(m)
# print(count_negative_and_zeros(m))