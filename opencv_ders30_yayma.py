import cv2 as cv
import numpy as np

cekirdek=np.ones((5,5),np.uint8)

resim=cv.imread("j.png",0)
# morfoloşik işlemlerde resmin  gri formatta olması gerekir

son_hal=cv.dilate(resim,cekirdek,iterations=1)
# dilate=yayma fonksiyonudur

cv.imshow("Orijinal",resim)
cv.imshow("Yayma",son_hal)
cv.waitKey(0)