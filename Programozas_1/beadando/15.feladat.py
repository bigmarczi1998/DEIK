"""

Marci 21 192
Zoli 22 178
Krisztián 30 170
Marci 22 189
István 90 170
Marci 21 180
Zoli 20 190


"""


def rendezett_tuple():
    line = input('név életkor magasság:\n')

    lst = []
    tpl = []

    while line != '0':
        lst.append(line.split())
        tpl.append(tuple(line.split()))
        line = input()

    # tpl = tuple(tpl)

    # print(*tpl, sep='\n')
    # print('*' * 50)

    for i in range(len(lst)):
        lst[i][0] = str(lst[i][0])
        lst[i][1] = int(lst[i][1])
        lst[i][2] = int(lst[i][2])

    # print(lst)

    sorted_by_name = sorted(lst, key=lambda poz: (poz[0], -poz[1], poz[2]))
    # lambda fgv-el dolgozom, lista rendezes miatt
    # poz: utan a visszateresi erteket adom meg
    # 9.gyakorlati ora

    for x in range(len(sorted_by_name)):
        sorted_by_name[x][0] = str(sorted_by_name[x][0])
        sorted_by_name[x][1] = str(sorted_by_name[x][1])
        sorted_by_name[x][2] = str(sorted_by_name[x][2])

    for e in range(len(sorted_by_name)):
        sorted_by_name[e] = tuple(sorted_by_name[e])

    sorted_by_name = tuple(sorted_by_name)

    print(*sorted_by_name, sep='\n')


if __name__ == '__main__':
    rendezett_tuple()
