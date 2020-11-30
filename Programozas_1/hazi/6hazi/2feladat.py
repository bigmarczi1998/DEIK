import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


def rgb2gray(image):
    """

    :rtype: zold_eltuntet
    """
    gray = np.uint8(0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2])
    return gray


def sorok_torol(image):
    avg_kep = np.mean(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > avg_kep:
                image[i, j] = 255
            else:
                image[i, j] = 0


def main():
    image = img.imread('flowers.jpg')
    gray = rgb2gray(image)
    sorok_torol(gray)
    plt.imshow(gray, cmap="gray")
    plt.imshow(gray, cmap="gray")
    plt.show()


if __name__ == '__main__':
    main()