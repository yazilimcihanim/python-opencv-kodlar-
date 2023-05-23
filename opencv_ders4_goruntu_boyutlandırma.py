import cv2

resim=cv2.imread("images.jpg")
boyut=(608,1024)
boyutlandirilmis_hal=cv2.resize(resim,boyut)
# görüntümün boyutunu değiştirmek istersem bunu
# "resize" fonksiyonu bile yaparım
# bir boyut belirlerim liste olarak,yukarıdaki  "boyut" listesi  gibi
# sonra bu  resize içinde kullanılır

cv2.imshow("goruntu penceresi",resim) # normal resmimi penceresi
cv2.imshow("boyutlandırılmış resim",boyutlandirilmis_hal) #boyutlandırılmış resmin penceresi

cv2.imwrite("yeni.jpg",boyutlandirilmis_hal) #yeni boyuttaki resmikadetme

cv2.waitKey(0)