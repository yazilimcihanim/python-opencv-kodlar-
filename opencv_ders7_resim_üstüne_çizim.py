import cv2

oku=cv2.imread("images.jpg")

# resim çizmek için rectangle foksiyonu kullanılır
cv2.rectangle(oku,(12,12),(150,150),(0,255,0),2)
#rectangle(matrisin_adı,(y eksen sınırları),(x eksen sınırları),(renk),kalınlık)
# renke için=>> 255,0,0=mavi, 0,0,255=kırmızı, 0,255,0=yeşildir


cv2.imshow("pencere",oku)
cv2.waitKey(0)