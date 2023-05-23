import cv2 as cv
import numpy as np
#açma= ilkin aşındırma sonrada yayma işlemi yapılır


cekirdek=np.ones((5,5),np.uint8) # çekirdek oluşturduk

resim=cv.imread("acma.JPG",0)

resim2=cv.imread("kapama.JPG",0)
#resimlerimizi griye dönüştürdük

#acma=cv.morphologyEx(resim,cv.MORPH_OPEN,cekirdek)
# açma fonksiyonu=morphology dir


# acma işleminin doğru çalıştığından emin olmak istiyorsak
# aşağıdaki kodları çalıştırırız
#islem1=cv.erode(resim,cekirdek,iterations=1)   #aşındırma
#islem2=cv.dilate(islem1,cekirdek,iterations=1) # yayma


kapama=cv.morphologyEx(resim2,cv.MORPH_CLOSE,cekirdek)
# kapama fonksiyonu=morhpology
# ilk yayma sonra aşındırma işlemini yapar


cv.imshow("resim",resim)
#cv.imshow("Acma",acma)

#cv.imshow("Acma",islem2)
cv.imshow("Orijinal",resim2)
cv.imshow("Kapama",kapama)
cv.waitKey(0)