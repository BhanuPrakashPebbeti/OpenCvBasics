import cv2 as c

cap = c.VideoCapture("http://192.168.1.102:8080/video")
while True:
    success ,img = cap.read()
    resize = c.resize(img,(1080,640))
    c.imshow("Video",resize)
    if c.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
c.destroyAllWindows()
