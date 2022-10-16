import cv2
import matplotlib.pyplot as plt
import numpy as np


"""
gamma işlemi parlaklık artırma olarakda bilinmektedir

"""

resim=cv2.imread("ayasofya.jpg")
resim=cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)


yeni_resim=resim.copy()
for yuk in range(resim.shape[0]):
    for gen in range(resim.shape[1]):
        for kanal in range(resim.shape[2]):
            yeni_resim[yuk,gen,kanal]=np.clip(1.3*resim[yuk,gen,kanal]+15,0,255)
while True:
    cv2.imshow("orijinalresim ",resim)
    cv2.imshow("yeni resim ", yeni_resim)

    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()

