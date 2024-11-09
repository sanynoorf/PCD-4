import imageio.v3 as imageio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

image = imageio.imread('beruang.jpg')  

if image.ndim == 3: 
    grayscale_image = np.dot(image[..., :3], [0.299, 0.587, 0.114])
else:
    grayscale_image = image 

filtered_image = ndimage.gaussian_filter(grayscale_image, sigma=2)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(grayscale_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Gambar Setelah Gaussian Filter")
plt.imshow(filtered_image, cmap='gray')

plt.show()