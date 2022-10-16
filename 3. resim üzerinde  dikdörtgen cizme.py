import numpy as np
import cv2

import matplotlib.pyplot as plt

bos_resim=cv2.imread("ayasofya.jpg")

cv2.rectangle(img=bos_resim,pt1=(200,100),pt2=(10,30),color=(80,80,205),thickness=2)

while True:
    cv2.imshow("resimpenceresi",bos_resim)
    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()
