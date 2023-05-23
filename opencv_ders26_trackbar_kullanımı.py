

import cv2
import numpy as np

#cv2.createTrackbar("trackbar_adı","pencere_adı",başlangıç_degeri(0),max_deger,fonksiyon)

siyah=np.zeros((480,640,3),np.uint8) #görüntüyü siyah yapar
cv2.namedWindow("pencere")
def fonk(x):
    print(x)

cv2.createTrackbar("Ali","pencere",0,255,fonk)
#sonsuz defa çalışır

while True:

    ali=cv2.getTrackbarPos("Ali","pencere") # trackbarın adı,görüntülemek istediğim pencere adı
    cv2.imshow("pencere",siyah)
    cv2.waitKey(1)

