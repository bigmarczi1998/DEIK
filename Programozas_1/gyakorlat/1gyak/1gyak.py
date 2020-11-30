# 1
# def main():
#     n = int(input("Kérek egy számot: "))  # int az egy tipuskonverzio
#     while n != 0:
#         if n % 2 == 0:  # szam paros | maradeknelkuli osztas
#             print("Páros")
#         else:
#             print("Páratlan")
#         n = int(input("Kérek egy számot: "))
#
#
# main()

# 2
# import math modszer is lehet math.gcd(a,b)
# def lnko(a,b):
#     if b<a:
#         a,b=b,a
#     div=1
#     for i in range(2,a+1):
#         if a%i==0 and b%i==0:
#             div=i
#     return div
#
# sor=input("kerek egy szamot: ")
# a,b=sor.split() #alapertelmezett modokon szokozokkel megy a split
# print(lnko(int(a),int(b))) #figyeljuk hogy behivasnal meg a es b csak sztringek

# 3
# def ponttav(x1,y1,x2,y2):
#     d=(((x1-x2)**2)+(y1-y2))**1/2
#     return d
# pontok=("kerek egy x1 y1 x2 y2 koordinátát: ")
# x1,y1,x2,y2=pontok.split()
#
# from math import sqrt, pow
# x=input("x:")
# y=input("y:")
# x1,y1=x.split()
# x2,y2=y.split()
# print(sqrt(pow(int(x1)-int(x2),2)+pow(int(y1)-int(y2),2)))

# 4
# szamjegyek osszeadasa
# n=input("kerek egy szamot: ")
# sum=0
# for i in n:
#     sum+=int(i)
# print(sum)
#
# #vagy while ciklussal
# b=int(input("kerek egy szamot: "))
# sum=0
# while b>0:
#     sum+=b%10
#     b=b//10
# print(sum)

# 5
# vesszovel elvalasztva kerjunk be szavakat, majd ezeket listaba tarolni, splittel vesszo szerint elvalasztjuk
# def rendezett_szavak(lista):
#     eredmeny_lista=list()
#     for szo in lista:
#         if szo not in eredmeny_lista:
#             eredmeny_lista.append(szo)
#     eredmeny_lista.sort() #.sort helyben rendezi a listankat
#     return eredmeny_lista
# szavak=input("Kerem a szavakat: ")
# lista=list(szavak.split(','))
# print(rendezett_szavak(lista))

# 6
# def elso_harom(szo):
#     if len(szo)<3:
#         return szo
#     else:
#         return szo[:3]
# szo=input("Kerek egy szot: ")
# print(elso_harom(szo))
