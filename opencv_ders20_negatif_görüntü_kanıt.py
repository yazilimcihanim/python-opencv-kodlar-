import cv2

def tersine_cevirme(matris):
    return cv2.bitwise_not(matris)


resim=cv2.imread("images.jpg")
ters=tersine_cevirme(resim)
tersinin_tersi=tersine_cevirme(ters)

cv2.imshow("resim",resim)
cv2.imshow("ters resim",ters)
cv2.imshow("trsinin tersi",tersinin_tersi)

cv2.waitKey(0)