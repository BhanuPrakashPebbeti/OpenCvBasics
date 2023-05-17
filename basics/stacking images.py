import cv2 as c
import numpy as np

img = c.imread("cards.jpg")
#img=c.resize(img1,(300,300))
grey = c.cvtColor(img,c.COLOR_BGR2GRAY)
hstack = np.hstack((img,img))
vstack=  np.vstack((grey,grey))

c.imshow("staked_image",hstack)
c.imshow("staked_image1",vstack)
c.waitKey(0)
