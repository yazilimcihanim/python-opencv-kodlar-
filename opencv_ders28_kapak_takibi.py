import cv2 as cv
import numpy as np
res=np.array((400,400,2),np.uint8)
cv.namedWindow("Trackbar")
def fonk(sayi):
    print(sayi)

cv.createTrackbar("azM","Trackbar",0,255,fonk)
cv.createTrackbar("cokM","Trackbar",0,255,fonk)
cv.createTrackbar("azY","Trackbar",0,255,fonk)
cv.createTrackbar("cokY","Trackbar",0,255,fonk)
cv.createTrackbar("azK","Trackbar",0,255,fonk)
cv.createTrackbar("cokK","Trackbar",0,255,fonk)
takip=cv.VideoCapture("takip.mp4")
while True:
    cv.imshow("Trackbar",res)
    kontrol,yakala=takip.read()
    azM = cv.getTrackbarPos("azM","Trackbar")
    cokM = cv.getTrackbarPos("cokM", "Trackbar")
    azY = cv.getTrackbarPos("azY", "Trackbar")
    cokY = cv.getTrackbarPos("cokY", "Trackbar")
    azK = cv.getTrackbarPos("azK", "Trackbar")
    cokK = cv.getTrackbarPos("cokK", "Trackbar")
    az=np.array([azK,azY,azM])
    cok=np.array([cokK,cokY,cokM])
    istenen=cv.inRange(yakala,az,cok)
    son=cv.bitwise_and(yakala,yakala,mask=istenen)
    cv.imshow("video",yakala)
    cv.imshow("istenen",istenen)
    cv.imshow("son hali",son)
    if cv.waitKey(20) & 0xFF==ord("q"):
        break
    cv.waitKey(1)