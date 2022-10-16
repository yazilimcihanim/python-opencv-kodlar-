import cv2
import matplotlib.pyplot as plt

# birden fazla pencereyi ekranda gösterebiliriz

resim1=cv2.imread("ayasofya.jpg")
resim1=cv2.cvtColor(resim1,cv2.COLOR_BGR2RGB)
resim2=resim1.copy()
resim3=resim1.copy()
resim4=resim1.copy()

pencere=plt.figure(figsize=(5,8))
pencere.add_subplot(2,2,1)
plt.imshow(resim1)

pencere.add_subplot(2,2,2)
plt.imshow(resim2)

pencere.add_subplot(2,2,3)
plt.imshow(resim3)

pencere.add_subplot(2,2,4)
plt.imshow(resim4)

f,eksen=plt.subplots(2,2)
eksen[0,0].imshow(resim1)
eksen[0,1].imshow(resim2)
eksen[1,0].imshow(resim3)
eksen[1,1].imshow(resim4)


while True:
    cv2.imshow("resimpenceresi1",resim1)
    cv2.imshow("resimpenceresi2", resim2)
    cv2.imshow("resimpenceresi3", resim3)
    cv2.imshow("resimpenceresi4", resim4)
    # 27== esc tuşu. ekran çıktısını kapatmak için esc tuşuna basmalısınız :))
    if cv2.waitKey(10) & 0xFF ==27:
        break

cv2.destroyAllWindow()
