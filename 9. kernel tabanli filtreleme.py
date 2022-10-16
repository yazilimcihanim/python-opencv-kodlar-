import cv2
import numpy as np


resim=cv2.imread("ayasofya.jpg")
resim=cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)
kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

sonuc=cv2.filter2D(resim,-1,kernel)


while True:
    cv2.imshow("sonuc",sonuc)
    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()
