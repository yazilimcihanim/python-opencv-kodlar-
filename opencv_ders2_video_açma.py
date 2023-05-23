import cv2

video=cv2.VideoCapture("ACMAK İSTEDİĞİNİZ VİDEONUN ADINI BURAYA YAZINIZ.mp4")
#videomun adını ve uzantısını
# videocapture  fonksiyona ekleyip değişkene atadım.

while True:
    kontrol, yakala=video.read()
    cv2.imshow("goruntu",yakala)

    # videomu erkanda göstermek için if bloğu açtım
    if cv2.waitKey(20) & 0xFF==ord("p"):
        break