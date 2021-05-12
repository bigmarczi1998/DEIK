import numpy as np
def most_number(file_name):
    out_file=open("{}.txt".format(file_name),"w")
    number = np.random.randint(1, 10, size=10)
    print('Vektor:{}'.format(number),file=out_file)

    most_number=np.bincount(number).argmax()
    print('A legtobbet szereplo szam: {}'.format(most_number),file=out_file)

    counts=np.bincount(number).max()
    print('Elofordulasok szama: {}'.format(counts),file=out_file)

    out_file.close()

file_name=str(input('Fájlnév:'))
most_number(file_name)