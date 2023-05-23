import cv2

#images.jpg dosyamın yüksekliğini derinliğini ve genişliini öğrenivcez

oku=cv2.imread("images.jpg")
(yukseklik,genislik,derinlik)=oku.shape
# sıra önemli çünkü shape fonksiyonunda
# ilk kısım yüksekliğe aittir, ikinci kısım genişlik ve üç de derinliktir

print(f"yukseklik: {yukseklik} genislik:{genislik} derinlik:{derinlik}")

cv2.imshow("goruntule",oku)
# görüntüle adındaki pencerede oku matrisini görüntüler


cv2.waitKey(0)
