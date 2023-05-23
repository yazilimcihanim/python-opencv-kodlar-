import cv2
# bu kodla kırmızı yeşil ve mavinin piksellerine ulaşabilirim


resim123=cv2.imread("images.jpg")
(mavi,yesil,kirmizi)=resim123[110,20]
# her zaman renklerin sırası böyle
print("kırmızı:{} mavi:{} yeşil:{}".format(kirmizi,mavi,yesil))