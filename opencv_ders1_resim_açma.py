import cv2 # opencv kütüphanemizi kullanırken CV2 ile import ediyoruz.


logo=cv2.imread("images.jpg",)
# açmak istediğimiz resimin adını imread fonksiyonumuzun içine ekleyip
#logo adındaki değişkene atadık

cv2.imshow("logo ",logo)
# imshow fonkiyonu ile pencere tanımlıyoruz
# yazdığımızı ilk parametre pencere adı
# ikincisi ise fotoğrafımızı atadığımız değişken adı

cv2.waitKey(0)
# penceremizin ekranda kalmasını sağlıyor
# saniye cinsinden parametre alıyor
# '0'(sıfır) sonsuz anlamına geliyor





