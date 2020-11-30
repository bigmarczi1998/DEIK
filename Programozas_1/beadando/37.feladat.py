def rendezett_lista(lst):
    db = 0
    s = 0
    for i in range(len(lst)):
        s += lst[i]
        db += 1

    avg = s / db

    # print(avg)

    lst_new = []
    for x in range(len(lst)):
        if (lst[x] > avg) or (lst[x] == 0):
            lst_new.append(lst[x])

    # print(lst_new)

    lst_new.sort()

    # print(lst_new)

    for y in range(len(lst_new)):
        lst_new.append(lst_new.pop(lst_new.index(0)))
        # pop fugv (adatszerkezet), ami eltavolit es visszater a lst-bol az utolso erteket vagy az adott index erteket
        # ebben az esetben valamely index 0-as elemet a vegere csatolja

    print('Kimenet: ', lst_new)


def rendezetlen_lista():
    lst = [7, 10, 0, 9, 11, 0, 17]
    print('Bemenet: ', lst)
    return rendezett_lista(lst)


if __name__ == '__main__':
    rendezetlen_lista()
