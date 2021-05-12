import matplotlib.pyplot as plt
import numpy as np


def main():

    my_file = open("arfolyam.txt", "r")
    temp = my_file.read().splitlines()
    half1 = temp[0].split()
    half2 = temp[1].split()

    x = np.arange(1, 11)

    money1 = []
    money2 = []

    for i in range(len(half1)):
        money1.append(float(half1[i]))

    for j in range(len(half2)):
        money2.append(float(half2[j]))

    plt.plot(x, money1, label="pénznem1")
    plt.plot(x, money2, label="pénznem2")
    plt.title("Árfolyamváltozás")
    plt.ylabel('HUF')
    plt.ylabel('napok')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()