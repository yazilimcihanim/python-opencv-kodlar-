import cv2

resim=cv2.imread("images.jpg")
kirpma=resim[10:100,20:300] # kıırpma işlemi bu şekilde yapılır
# önce y başlangıç:y bitiş  sonra x ekseni yazılır
cv2.imshow("pencere",resim)
cv2.imshow("kırpılmış",kirpma)
cv2.waitKey(0)