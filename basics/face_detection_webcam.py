import cv2 as c
 
faceCascade= c.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
cap = c.VideoCapture(0)
cap.set(3,640) #height id = 3
cap.set(4,480) #width id = 4
cap.set(10,25) #brightness id = 10
while True:
    success ,img = cap.read()
    imgGray = c.cvtColor(img,c.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,5)
    for (x,y,w,h) in faces:
        c.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    c.imshow("Result", img)
    if c.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
c.destroyAllWindows()