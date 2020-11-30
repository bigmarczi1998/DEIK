def atlag(my_file):
    for line in my_file:
        tmp=line.split()
        db=0
        ossz=0
        for szam in tmp:
            if int(szam)>0:
                ossz+=int(szam)
                db+=1

        if ossz==0:
            print('Nem számolható átlag!')
        else:
            print(ossz/db)

try:
    my_file = open("szamok.txt", "r")
    atlag(my_file)
    my_file.close()
except FileNotFoundError:
    print('Rossz formatum')