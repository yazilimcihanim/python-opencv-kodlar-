import cv2  # opencv kütüphanemizi dahil ediyoruz

#circile fonksiyonu ile  daire oluşturabiliriz
taze_muhendis=cv2.imread("taze_muhendis.jpg")
merkez=(65,70)
renk=(125,120,20)  #
cv2.circle(taze_muhendis,merkez,70,renk,7) #kalem kalınlığını -1 yazarsam dairenin içi dolu olur
#circle(matris_adı,merkez,yarıçap,renk,kalem_kalınlığı)


cv2.imshow("taze muhendis site logosu ",taze_muhendis)
cv2.waitKey(0)


