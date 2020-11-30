def words(lista):
    db = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                db += 1
    return db


lst = ['abc', 'xxy', 'alma', 'auto']
ossz = 0
for i in lst:
    ossz += words(i)
print(ossz)
