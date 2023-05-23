import cv2

resim=cv2.imread("images.jpg")
bulanik=cv2.GaussianBlur(resim,(5,5),0) # resmi bulanıklaştıran fonksiyon
#(5,5) olan kısım bulanıklığın yoğunluğudur...
# ve ÇİFT SAYILARI KULLANAMASINIZ( 2,2   4,4  6,6  8,8 gibi değerleri veremezsiniz


cv2.imshow("resim",resim)
cv2.imshow("bulanık",bulanik)

cv2.waitKey(0)