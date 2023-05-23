import cv2 as cv
import numpy as np

cekirdek=np.ones((5,5),np.uint8)
#(5,5)= çekirdek büyüklüğüdür ki
#marifet çekirdek büyüklüğündedir

resim=cv.imread("images.jpg",0) # resmimizi gri moda çevirdik

#aşındırma işlemi için resmi önce gri moda çevirmeliyiz
asindirma=cv.erode(resim,cekirdek,iterations=7)
cv.imshow("orijinal",resim)
cv.imshow("asinmis resim)",asindirma)

cv.waitKey(0)
