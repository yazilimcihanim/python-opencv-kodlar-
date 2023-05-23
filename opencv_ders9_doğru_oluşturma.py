import cv2

oku=cv2.imread("images.jpg")

# doğru parçası oluşturmak için line fonksiyonu kullanılır
nok1=(50,95) #(x,y) noktaları
nok2=(80,95)
renk=(120,23,70)
kalinlik=8
cv2.line(oku,nok1,nok1,renk,kalinlik)
#line(matris_adı,nokta1,nokta2,renk,kalem_kalınlığı)

cv2.imshow("pencere",oku)
cv2.waitKey(0)