import cv2 as c

cap = c.VideoCapture(0)
cap.set(3,640) #height id = 3
cap.set(4,480) #width id = 4
cap.set(10,25) #brightness id = 10
while True:
    success ,img = cap.read()
    c.imshow("Video",img)
    if c.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
c.destroyAllWindows()

