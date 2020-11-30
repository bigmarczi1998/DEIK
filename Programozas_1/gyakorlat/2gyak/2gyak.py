# fajlkezeles

# https://github.com/snorbi95/Programming1

# read-r,write-w,append-a(letezot megnyit es azt lehet boviteni)
# egyes sorok feldolgozasa | for line in my_file: azutan a nyitott filet be kell zarni close
# fajlba kiiras | out_file=open(output.txt","w)
# elszallas megakadalyozasa | try (futtatni kivant kodreszlet) except (kivetel amit ne)
# egy egy mvelet hibakodjai except FileNotFoundError | Kivételezés
# finally blokk mindig lefut hibatol fuggetlenul
# kivetel dobasa | hibageneralas | try és except

# 1
# kivetelkezeles(milyen hibat kell elkapni) a ValueError kell lekezelni a programunknak
# ez csak egy erteket tud kiiertekelni ezert while true kell | ezzel mar folyamatos
# while True:
#     try:
#         x=input("Kerek egy szamot:")
#         x=int(x)
#         print(x)
#         break
#     except ValueError: #ezt akarom elkapni
#         print("A megadott ertek nem szam!")

# 2
# file=open("input.txt","r")
# try:
#     for line in file:
#         print(line,end="") #print utoatikusan berak egy uj sort, ezt a kovetkezokeppen tudjuk megoldani | print(line,end="") vagy line.rstrip() ez az adott stringnek a sorra leveszi az entert vagy az elotte levo karaktereket
# except FileNotFoundError:
#     print("Nincs ilyen fajl!")
# finally:
#     file.close()

# 3
# def number_of_lannisters(file):
#     x=0 #valtozo, hanyszor szerepel benne a szavunk
#     for line in file:
#         tmp=line.split() #feldarabolos listank tmp
#         for word in tmp:
#             if "Lannister" in word:
#                 x+=1
#     return x
#
# try:
#     my_file=open("input.txt","r")
#     print("A Lannister szo {} alkalommal talalhato a fajlban!".format(number_of_lannisters(my_file)))
#     my_file.close()
# except FileNotFoundError:
#     print("megadott fajl nem talalhato")

# 4
kis betut naggya es forditva
ch.islower() keres
ch.isupper() keres
larakter atalakitasa #ch.lower() #ch.upper()
kiiratas fajlba | print.....,file=outputfile

import string
# def abc_change_ABC():
#     my_file = open("input.txt", "r")
#     out_file = open("output.txt", "w")
#     for line in my_file:
#         new_str = ""
#         for ch in line:
#             if ch.islower():
#                new_str+=ch.upper()
#             if ch.isupper():
#                 new_str+=ch.lower()
#             else:
#                 new_str+=ch
#         print(new_str,file=out_file,end="")
#     my_file.close()
#     out_file.close()
# try:
#     abc_change_ABC()
# except FileNotFoundError:
#     print("megadottt fajl nem talalhato")

# 5
# import string
#
#
# def find_longest_words(my_file):
#     out_file = open("LongestWords.txt", "w")
#     max_hossz = 0
#     leghossz_szavak = []
#     jelek = [",.!-"]
#     for line in my_file:
#         new_str = ""
#         for ch in line:
#             if ch not in string.punctuation:  # tartalmazza az osszes nemkivanatos irasjelet
#                 new_str += ch
#         tmp = line.split()
#         for word in tmp:
#             if len(word) > max_hossz:
#                 leghossz_szavak = []
#                 max_hossz = len(word)
#                 leghossz_szavak.append(word)
#             elif len(word) == max_hossz:
#                 leghossz_szavak.append(word)
#
#     print("A leghosszabb szo {} karakterbol all.".format(max_hossz), file=out_file)
#     for szavak in leghossz_szavak:
#         print(szavak, file=out_file)
#     out_file.close()
#
#
# try:
#     my_file = open("input.txt", "r")
#     find_longest_words(my_file)
#     my_file.close()
# except FileNotFoundError:
#     print("hiba")
