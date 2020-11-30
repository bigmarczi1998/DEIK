import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


# norbi
def rgb2gray(image):
    # egesz ertekek(int) #zarojelben a sulyok (rgb) most a pirosat
    gray = np.uint8(0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2])
    return gray


image = img.imread('flowers.jpg')
gray = rgb2gray(image)
plt.subplot(1, 2, 1)  # elhelyezes egy feluleten, sor oszlop hely
plt.imshow(image)
plt.subplot(1, 2, 2)
# plt.imshow(gray) #piros szinek elonyben
plt.imshow(gray, cmap='gray')  # szurkearnyalatos
plt.show()


# marcsi
def RGB2gray(img):
    gray = np.uint8(img[:, :, 0] * 0.2989 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.114)
    return gray


def main():
    img = plt.imread('flowers.jpg')
    plt.imshow(img)
    plt.show()
    gray = RGB2gray(img)
    plt.imshow(gray, 'gray')
    plt.show()


if __name__ == '__main__':
    main()
