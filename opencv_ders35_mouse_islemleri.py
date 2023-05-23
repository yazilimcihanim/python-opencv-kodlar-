import cv2
import numpy as np

def mouse(etkinlik,x,y,flags,param):
    if(etkinlik==cv2.EVENT_MOUSEMOVE):
        print("MOUSE RESİM ÜSTÜNDE!!")
    elif(etkinlik==cv2.EVENT_LBUTTONDOWN):
        print("sol tıka basıldı")
    elif(etkinlik==cv2.EVENT_RBUTTONDOWN):
        print("sağ tıka basıldı")

resim=np.zeros((400,400,3),np.uint8)
# np modulu ile sıfır matrisi oluşturduk
#kordinatlarını ve kanal sayısını giriyoruz
# daha sonra bit degerini vermeliyiz
# genellikle 8 bitlik ile çalışırız(uint8)


# mouse işlemi yapacağımız
# pencereyi oluşturmalıyız
cv2.namedWindow("mouse",cv2.WINDOW_AUTOSIZE)

# mouse işlemini gerçekleştiren fonksiyon
cv2.setMouseCallback("mouse",mouse)
#cv2.setMouseCallback("pencereadı",fonksiyon adı)


cv2.imshow("mouse",resim)

cv2.waitKey(0)


