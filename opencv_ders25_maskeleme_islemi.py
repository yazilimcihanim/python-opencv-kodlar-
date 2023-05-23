#inrange fonksiyonu sayesinde
# belirli aralıktaki değerleri çıktı olarak alabiliriz
# inrange fonksiyonunu kullanabilmek için numpy modulunu kullanmalıyız
# ve görüntüyü griye dönüştürmeliyiz



#önceki derste belirli aralıkta etelde edilen çıktı renksizdi
# bu derste  aynı çıktıyı renki elde edicez


import cv2
import numpy
resim=cv2.imread("images.jpg")

az=numpy.array([20,10,25])
cok=numpy.array([255,255,255])
istenen=cv2.inRange(resim,az,cok)

# fonksiyon sayesinde istenen kısım renkli hale gelir
sonuc=cv2.bitwise_and(resim,resim,mask=istenen)

cv2.imshow("resim",resim)
cv2.imshow("inrange",istenen)
cv2.imshow("sonuç",sonuc)
cv2.waitKey(0)

