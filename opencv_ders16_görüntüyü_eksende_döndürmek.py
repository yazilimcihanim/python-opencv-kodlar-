import cv2

resim=cv2.imread("images.jpg")

#görüntüyü eksenlerde hareket ettirmek için flip fonksiyonu kullanılır
dikine_döndürme=cv2.flip(resim,0) # y ekseninde hareket etrir
yatay_döndürme=cv2.flip(resim,1) # x ekseninde döner
tüm_döndürmek=cv2.flip(resim,-1) # tüm eksenlerde döner
cv2.imshow("orijinal hal ",resim)
cv2.imshow("dikine_döndürme",dikine_döndürme)
cv2.imshow("yatay_döndürme",yatay_döndürme)
cv2.imshow("tüm_döndürmek",tüm_döndürmek)
cv2.waitKey(0)

