import numpy as np
import cv2

import matplotlib.pyplot as plt

# cv2 ile açıldı
resim=cv2.imread("ayasofya.jpg")
print(type(resim))
print(resim.shape)

plt.imshow(resim)
