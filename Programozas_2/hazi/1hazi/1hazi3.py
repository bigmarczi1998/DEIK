def elso_oszthato(list):
    x = list[0]
    new_list = []
    for i in list:
        if i % x == 0:
            if i not in new_list:
                new_list.append(i)
    return set(new_list)


lista = [4, 7, 8, 8, 15, 24, 101, 88, 4]
print(elso_oszthato(lista))
