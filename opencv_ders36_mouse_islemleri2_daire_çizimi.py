import cv2
resim=cv2.imread("images.jpg")
def daire_ciz(etkinlik,x,y,flags,param):
    if etkinlik==cv2.EVENT_LBUTTONDOWN:
        cv2.putText(resim,"Daire olusturdum!",(x-40,y-40),cv2.FONT_ITALIC,1,(0,255,0),5) # yazı tipi
        cv2.circle(resim,(x,y),35,(255,0,0))

cv2.namedWindow("Pencere",cv2.WINDOW_AUTOSIZE) # pencere oluşturduk
cv2.setMouseCallback("Pencere",daire_ciz) # pencere adı, oluşturduğumuz fonksiyon
while True:
    cv2.imshow("Pencere",resim)
    if(cv2.waitKey(20)==27): # 27==esc tuşudur  pencereyi kapatmak için esc ye basmalıyız
        break
cv2.destroyAllWindows() # pencereleri yok eder