import cv2



resim=cv2.imread("images.jpg")

# resim üstüne yazı yazan fopnksiyon
#putText fonksiyonudur
resim=cv2.putText(resim,"yazilimci.hanim",(1,60),cv2.FONT_ITALIC,1,(255,34,56),3)
#cv2.putText(yazı_yazılacak_matrix_adı,yazılacak_yazı,(x,y),yazı_fontu,harfler_arası_mesafe,renk,kalınlık)


cv2.imshow("pencere",resim)
cv2.waitKey(0)