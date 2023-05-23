import cv2

#resim=cv2.imread("images.jpg") veya...

isim="images.jpg"

resim=cv2.imread(isim)
medyan=cv2.medianBlur(resim,7)
# gürültü azaltan fonksiyon
# ikinci değer, görültü azaltma oranıdır 

cv2.imshow("resim",resim)
cv2.imshow("medyan",medyan)

cv2.waitKey(0)