import cv2 as c
 
faceCascade= c.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img = c.imread('ece-batch.jpeg')
imgGray = c.cvtColor(img,c.COLOR_BGR2GRAY)
 
faces = faceCascade.detectMultiScale(imgGray,1.1,5)
 
for (x,y,w,h) in faces:
    c.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 
c.imshow("Result", img)
c.waitKey(0)