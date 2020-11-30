"""
alma ablak pohar kozepertek amerikai valasztasi rendszer
"""

import string
import math


def rendezett_szavak(lst):
    list = []
    for szo in lst:
        if szo not in list:
            list.append(szo)

    # print(list)

    abc = string.ascii_lowercase

    # print(abc)

    min_first = ''
    min_last = ''
    min_ch = ''
    min_distance = math.inf

    for x in range(len(list)):
        seq = ''.join(sorted(list[x]))
        # sequence / sorrendbe allitom a szavak betuit
        # print(seq)
        for i in range(len(abc)):
            if seq[0] == abc[i]:
                min_first = i + 1
                # a szo elso abc tagja
                # print(min_first)
            if seq[-1] == abc[i]:
                min_last = i + 1
                # a szo utolso abc tagja
                # print(min_last)
        distance = min_last - min_first
        # a szo elso es utolso abc tagjanak tavolsaga
        # print(distance)
        if min_distance > distance:
            min_distance = distance
            min_ch = list[x]
            # megvizsgalom, melyik a legkissebb tavolsag

    print(min_ch)


def rendezetlen_szavak():
    words = str(input('szavak: '))
    lst = list(words.split(' '))
    return rendezett_szavak(lst)


if __name__ == '__main__':
    rendezetlen_szavak()
