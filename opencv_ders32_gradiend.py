
# gradient nedir?== yayma-aşındırmadır(ikisinin farkıdır)
# görüntünün iskeletini çıkartabiliriz


import cv2 as cv
import numpy as np

cekirdek=np.ones((5,5),np.uint8)
resim=cv.imread("j.png",0)   #görünütüyü griye çevirdik

#gradient fonksiyonu ile graient  işlemi
gradient=cv.morphologyEx(resim,cv.MORPH_GRADIENT,cekirdek)



cv.imshow("Orijinal",resim)
cv.imshow("Gradient",gradient)
cv.waitKey(0)