import cv2

resim=cv2.imread("images.jpg")#yukseklik: 160 genislik:160 derinlik:3
yukseklik=160
genislik=160
merkez_nokta=(genislik/2,yukseklik/2) # görüntümün orta noktası
d=cv2.getRotationMatrix2D(merkez_nokta,-30,1.0) # "-"(eksili olunca sola döner)
#cv2.getRotationMatrix2D(matris_adı,dönme_açısı,scale(genelde 1 olur)))
dondurma=cv2.warpAffine(resim,d,(genislik,yukseklik))

cv2.imshow("pencere1",dondurma)

cv2.waitKey(0)

