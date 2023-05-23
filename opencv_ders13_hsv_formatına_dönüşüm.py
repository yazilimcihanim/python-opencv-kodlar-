import cv2
#hsv görüntü=renkleri belirgenliştirilmesi olayıdır

resim=cv2.imread("images.jpg")


hsv_format=cv2.cvtColor(resim,cv2.COLOR_BGR2HSV)
#bu kodla görüntü hsv formatına dönüştü

cv2.imshow("pencere",resim)
cv2.imshow("hsv RESİM ",hsv_format)
cv2.waitKey(0)