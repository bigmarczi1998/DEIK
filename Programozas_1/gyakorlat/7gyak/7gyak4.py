def dobokocka_szotar():
    dict = {}
    for i in range(1,7):
        for j in range(1,7):
            if (i + j) not in dict:
                dict[i + j] = [(i,j)]
            else:
                dict[i + j].append((i,j))
    return dict

dict = dobokocka_szotar()
length = 0
for key,value in dict.items():
    length += len(value)
    print("A {} osszeg elerheto: {}"\
          .format(key,value))
print(length)




#marcsi
import sys
"""Két dobókocka dobásából 36 különböző számpár kombináció állhat elő.
Hozzon létre egy szótárat, amelynek kulcsai a két kocka dobott értékeinek összege, 
(2-től 12-ig), a kulcsokhoz tartozó értékek pedig egy listában olyan tuple-ök, amelyek azokat 
a számpárokat tartalmazzák, amelyek összegeiből előállhat a kulcs értéke.

Pl.: 
2: [(1,1)]
3: [(2,1),(1,2)]
... stb

"""
def main():

    dict = {}
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            if d1 + d2 in dict:
                dict[d1 + d2].append((d1,d2))
            else:
                dict[d1 + d2] = [(d1,d2)]

    for k, v in dict.items():
        print(k, ":", v)



if __name__ == "__main__":
    main()