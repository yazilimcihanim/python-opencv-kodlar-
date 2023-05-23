import cv2
#canny algoritması binaryle işlem yaptığınıdan
#!!!görüntümüzü griye çevirmeliyiz

resim=cv2.imread("images.jpg",0) # görüntü gri oldu
kenar=cv2.Canny(resim,65,150) # canny fonksiyonu ile görüntümüzün kenarlarını buluyoruz
#cv2.Canny(matris_resim,eşikdeğer1,eşikdeğeri2)
#eşik değerlerini değiştirerek ne işe yaradığını  bulabilirsiniz

cv2.imshow("orijinal hal ",resim)
cv2.imshow("kenar hali",kenar)


cv2.waitKey(0)

