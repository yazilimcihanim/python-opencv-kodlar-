

#split=ayırmak
#merge=birleştirmek

import cv2 as cv
import numpy as np


resim=cv.imread("images.jpg")
sifir=np.zeros(resim.shape[:2],np.uint8)

b,g,r=cv.split(resim)
mavi=cv.merge([b,sifir,sifir])
yesil=cv.merge([sifir,g,sifir])
kirmizi=cv.merge([sifir,sifir,r])

cv.imshow("orijinal",resim)
cv.imshow("B",mavi)
cv.imshow("G",yesil)
cv.imshow("R",kirmizi)

cv.waitKey(0)
