import cv2 as c
import numpy as np
import time


cap = c.VideoCapture(0)
#cap = c.VideoCapture('http://192.168.43.1:8080/video')
time.sleep(3)
background=0
for i in range(30):
	ret,background = cap.read()

background = np.flip(background,axis=1)
while True:
    ret, img = cap.read()
    img = np.flip(img,axis=1)
    hsv = c.cvtColor(img, c.COLOR_BGR2HSV)

    if c.waitKey(1) & 0xFF==ord("q"):
        break
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = c.inRange(hsv,lower_red,upper_red)
    
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = c.inRange(hsv,lower_red,upper_red)
    
    mask = mask1+mask2
    
    img[np.where(mask==255)] = background[np.where(mask==255)]
    c.imshow('Display',img)

cap.release()
c.destroyAllWindows()
	
    
    
    

    