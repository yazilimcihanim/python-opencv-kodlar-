import cv2
import numpy as np

def olay_gerceklesti(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(bos_resim,(x,y),50,(0,0,255),-1) #sol tuş==kırmızı
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(bos_resim,(x,y),50,(0,255,0),-1) # sağ tuş== yeşil

cv2.namedWindow("resimpenceresi")
cv2.setMouseCallback("resimpenceresi",olay_gerceklesti)
bos_resim=np.zeros(shape=(640,640,3),dtype=np.uint8)

while True:
    cv2.imshow("resimpenceresi",bos_resim)
    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()

