import cv2
import matplotlib.pyplot as plt

# önce resmi boyutlandırdım
resim=cv2.imread("ayasofya.jpg",0)
boyut=(600,400)
boyutlandirilmis_hal=cv2.resize(resim,boyut)

#boyutlandırdığım resmi kullandım
ret1,th1=cv2.threshold(boyutlandirilmis_hal,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#otsu işlemi ile arka planı resimden ayırdık
#burda cami ve gökyüzü ayrıldı


while True:
    cv2.imshow("orijinal",boyutlandirilmis_hal)
    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()