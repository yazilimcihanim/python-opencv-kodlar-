import cv2
import matplotlib.pyplot as plt

"""
blur()
medianBlur()
boxFilter()
bilateralFilter()
bulanıklaştırma için kullanılan fonksiyonlar


ksize() == bulanıklaştırmaorasını belirler 
"""

resim1=cv2.imread("ayasofya.jpg",0)

sonuc1=cv2.blur(resim1,ksize=(3,3))
sonuc2=cv2.medianBlur(resim1,ksize=3)
sonuc3=cv2.GaussianBlur(resim1,ksize=(5,5),sigmaX=50)
sonuc4=cv2.bilateralFilter(resim1,d=7,sigmaColor=20,sigmaSpace=20)
sonuc5=cv2.boxFilter(resim1,ddepth=-10,ksize=(3,3))

while True:
    cv2.imshow("SONUC1", sonuc1)
    cv2.imshow("SONUC2", sonuc2)
    cv2.imshow("SONUC3", sonuc3)
    cv2.imshow("SONUC4", sonuc4)
    cv2.imshow("SONUC5", sonuc5)
    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()

