import cv2 as c
import numpy as np

img=c.imread("cards.jpg")
width,height = 250,350
pt1=np.float32([[111,219],[287,188],[154,482],[352,440]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = c.getPerspectiveTransform(pt1,pt2)
img1 = c.warpPerspective(img,matrix,(width,height))
c.imshow("output",img)
c.imshow("final",img1)
c.waitKey(0)