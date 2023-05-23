#görüntünün pikseliyle oynuyoruz

import cv2 as cv
import numpy as np

cv.namedWindow("Goruntu")
goruntu=np.zeros((450,495,3),np.uint8)
def fonk(sayi):
    print(sayi)

cv.createTrackbar("Mavi","Goruntu",0,255,fonk)
cv.createTrackbar("Yesil","Goruntu",0,255,fonk)
cv.createTrackbar("Kirmizi","Goruntu",0,255,fonk)

while True:
    cv.imshow("Goruntu",goruntu)
    mavi=cv.getTrackbarPos("Mavi", "Goruntu")
    yesil = cv.getTrackbarPos("Yesil", "Goruntu")
    kirmizi= cv.getTrackbarPos("Kirmizi", "Goruntu")
    goruntu[:]=[mavi,yesil,kirmizi]
    cv.waitKey(1) #waitKey(0) yazıncarenk değişimi yapmıyor
