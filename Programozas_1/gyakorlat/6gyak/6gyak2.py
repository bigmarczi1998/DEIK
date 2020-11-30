from matplotlib import pyplot as plt
import numpy as np


# def norbi
def hisztogram(mtx):
    hisz = np.zeros(256)
    for i in range(256):
        hisz[i] = np.sum(mtx == i)
    return h


mtx = np.random.randint(0, 256, (100, 100))
h = hisztogram(mtx)

plt.bar(range(256), h)
plt.show()



# marcsi
def histogramOfImg(m):
    h = np.zeros(256)
    for i in range(256):
        h[i] = np.sum(m == i)
    return h


def main():
    img = plt.imread('flowers.jpg')
    img = img[:, :, 0]
    print(histogramOfImg(img))
    plt.bar(range(0, 256), histogramOfImg(img))
    plt.show()


if __name__ == '__main__':
    main()