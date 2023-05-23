import cv2

resim=cv2.imread("images.jpg")

döndürme180=cv2.rotate(resim,cv2.ROTATE_180)
# 180 DERECE DÖNER GÖRÜNTÜ
döndürme90=cv2.rotate(resim,cv2.ROTATE_90_CLOCKWISE)
# SAAT YÖNÜNÜN TERSİNE 90 derece  döndürür


cv2.imshow("orijinal hal ",resim)
cv2.imshow("döndürme180",döndürme180)
cv2.imshow("döndürme90",döndürme90)

cv2.waitKey(0)

