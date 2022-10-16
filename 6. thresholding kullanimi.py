
import cv2
import matplotlib.pyplot as plt

orjinal= cv2.imread("ayasofya.jpg")
ret1, sonuc1=cv2.threshold(orjinal,127,255,cv2.THRESH_BINARY)
#127 den büyük alanların beyaz,küçük alanların ise siyah gösterir
ret1, sonuc2=cv2.threshold(orjinal,127,0,cv2.THRESH_TRUNC)
# 127 den büyük piksele sahip alanı beyaz,diğerlerini olduğu gibi gösterir
ret2, sonuc3=cv2.threshold(orjinal,127,0,cv2.THRESH_TOZERO)
#127 den küçük pikselli olanları siyah, büyük  pikselli olanları olduğu gibi bırakır

f, eksen= plt.subplots(4,1)
eksen[0].imshow(orjinal,cmap="gray")
eksen[1].imshow(sonuc1,cmap="gray")
eksen[2].imshow(sonuc2,cmap="gray")
eksen[3].imshow(sonuc3,cmap="gray")

#pencerenin ekranda durması için yazılmalı !!!!!!!!!!!!!!!!!!!!!!!!!!!
while True:
    cv2.imshow("orijinal",orjinal)
    cv2.imshow("sonuc1", sonuc1)
    cv2.imshow("sonuc2", sonuc2)
    cv2.imshow("sonuc3", sonuc3)
    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()

