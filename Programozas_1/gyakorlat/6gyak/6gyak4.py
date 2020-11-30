import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def rgb2gray(image):
    gray = np.uint8(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2])
    return gray

def sorok_torol(image):
    avg_kep = np.mean(image)
    row_avg = image.mean(axis = 1)
    for i in range(image.shape[0]):
        if row_avg[i] > avg_kep:
            image[i,:] = np.zeros(image.shape[1])

image = img.imread('flowers.jpg')
gray = rgb2gray(image)


plt.subplot(1,2,1)
plt.imshow(gray,cmap="gray")
plt.subplot(1,2,2)
sorok_torol(gray)
plt.imshow(gray,cmap="gray")
plt.show()