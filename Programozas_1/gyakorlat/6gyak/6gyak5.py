import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def rgb2gray(image):
    gray = np.uint8(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2])
    return gray

def mean_filter(image,mask_size):
    res_image = np.zeros_like(image)
    for i in range(mask_size,image.shape[0] - mask_size):
        for j in range(mask_size, image.shape[1] - mask_size):
            res_image[i,j] = np.mean(image[i - mask_size: i + mask_size, j - mask_size: j + mask_size])

    return res_image

image = img.imread('flowers.jpg')
gray = rgb2gray(image)

plt.subplot(1,2,1)
plt.imshow(gray,cmap='gray')
res_image = mean_filter(gray,15)
plt.subplot(1,2,2)
plt.imshow(res_image, cmap="gray")
plt.show()