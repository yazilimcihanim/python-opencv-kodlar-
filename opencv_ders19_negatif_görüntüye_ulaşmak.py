# bitwise_not fonksiyonu
#görüntüyü ters çeviriyor yani negatig görüntü oluşturuyor

import cv2 as cv

resim=cv.imread("images.jpg")
negatif=cv.bitwise_not(resim)#görüntüyü negatife çevirdik vedeğişkene atatık
cv.imshow("resim",resim)
cv.imshow("negatif görüntü",negatif)

cv.waitKey(0)