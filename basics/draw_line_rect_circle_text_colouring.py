import cv2 as c
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img1 = np.zeros((512,512,3),np.uint8)
img1[:]=255,0,0

c.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
c.rectangle(img,(106,106),(406,406),(0,0,255),5)
c.rectangle(img,(206,206),(306,306),(255,255,255),c.FILLED)
c.circle(img,(256,256),150,(255,255,0),5)
c.putText(img,"OPEN_CV",(300,25),c.FONT_HERSHEY_COMPLEX, 1,(0,150,0),1)

c.imshow("img",img)
c.imshow("img1",img1)
c.waitKey(0)


