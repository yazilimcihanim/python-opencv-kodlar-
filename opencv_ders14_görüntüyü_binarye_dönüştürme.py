import cv2
# resimi binarye dönüştürmke için önce gri formata çevirmeliyiz
resim=cv2.imread("images.jpg",0) # sıfır yazarak resmi grileştirdim

kontrol,binary=cv2.threshold(resim,150,255,cv2.THRESH_BINARY) # siyahlar önde
#cv2.threshold(matris_adı,eşik değer,max yoğunluk,tip,)
# eşik degerinin altı siyah üstü beyaz  olur
#max yoğunluk=255 olur genelde

kontrol,binary2=cv2.threshold(resim,150,255,cv2.THRESH_BINARY_INV)# beyaz renk ön planda 

#cv2.THRESH_BINARY_INV==cv2.THRESH_BINARY
#(renk olarak birbirlerinin zıttı yerleri boyar)

cv2.imshow("pencere1",binary)
cv2.imshow("pencere2",binary2)
cv2.waitKey(0)

