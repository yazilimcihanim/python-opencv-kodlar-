#inrange fonksiyonu sayesinde
# belirli aralıktaki değerleri çıktı olarak alabiliriz
# inrange fonksiyonunu kullanabilmek için numpy modulunu kullanmalıyız
# ve görüntüyü griye dönüştürmeliyiz

import cv2
import numpy
resim=cv2.imread("images.jpg")

az=numpy.array([0,10,0])
cok=numpy.array([255,255,255])
inrange=cv2.inRange(resim,az,cok)

cv2.imshow("resim",resim)
cv2.imshow("inrange",inrange)

cv2.waitKey(0)

