import cv2


resim=cv2.imread("images.jpg")


#resmin formatını değiştiren fonksiyon
#cvtColor() dur
gri_format=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

#resim=cv2.imread("images.jpg",0) da resmi griye dönüştürür

cv2.imshow("pencere",resim)
cv2.imshow("GRİ RESİM ",gri_format)
cv2.waitKey(0)