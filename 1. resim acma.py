import numpy as np
import cv2

import matplotlib.pyplot as plt

# matplotlib ile açıldı
resim=plt.imread("ayasofya.jpg")
print(type(resim))
print(resim.shape)

plt.imshow(resim)
