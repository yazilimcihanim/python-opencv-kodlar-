#bilateral  filtre yumuşaklığı artırmak içindir

import cv2

resim=cv2.imread("images.jpg")
bilateral=cv2.bilateralFilter(resim,85,93,93) # 93 olan yer resimi yumuşatma oranıdır
cv2.imshow("bilateral",bilateral)
cv2.imshow("orijinal resim ", resim )
cv2.waitKey(0)