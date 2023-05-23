#top hat nedir?==
# açma işleminden
# orıjınal görüntüyü çıkarma işlemidir

# blackhat nedir?==
# kapatma işleminden
# orijinal görüntüyü çıkarma işlemidir


import cv2 as cv
import numpy as np

cekirdek=np.ones((7,7),np.uint8)

resim=cv.imread("j.png",0)


top_hat=cv.morphologyEx(resim,cv.MORPH_TOPHAT,cekirdek)
black_hat=cv.morphologyEx(resim,cv.MORPH_BLACKHAT,cekirdek)


cv.imshow("Orijinal",resim)
cv.imshow("TopHat",top_hat)
cv.imshow("BlackHat",black_hat)
cv.waitKey(0)