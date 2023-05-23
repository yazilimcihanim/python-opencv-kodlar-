import cv2

resim=cv2.imread("images.jpg")
#kopyalama işlemi için copy() kullanılır
kopya=resim.copy()

cv2.imshow("orijinal",resim)
cv2.imshow("kopya",kopya)
cv2.waitKey(0)