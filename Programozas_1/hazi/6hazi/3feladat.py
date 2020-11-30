import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


def rgb2gray(image):
    """

    :rtype: zold_eltuntet
    """
    gray = np.uint8(0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2])
    return gray


def negative(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j] = -2 - image[i, j]


def main():
    image = img.imread('flowers.jpg')
    gray = rgb2gray(image)
    negative(gray)
    plt.imshow(gray, cmap="gray")
    plt.imshow(gray, cmap="gray")
    plt.show()


if __name__ == '__main__':
    main()