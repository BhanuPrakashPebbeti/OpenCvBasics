import cv2 as c
import numpy as np

kernel=np.zeros((5,5),np.uint8)
img1=c.imread("lena.png")
img = c.resize(img1, (300,300))

grey_img = c.cvtColor(img,c.COLOR_BGR2GRAY)                 #img --> grey
blur_img = c.GaussianBlur(grey_img, (7,7),0)                #img --> blur
canny_img = c.Canny(grey_img, 150,150)                      #img -->canny
dialated_img = c.dilate(canny_img,kernel,iterations=1)      #img -->dialated
eroded_img = c.erode(dialated_img, kernel, iterations=1 )   #img -->eroded
c.imshow("Grey_img",grey_img)
c.imshow("blur_img",blur_img)
c.imshow("canny_img",canny_img)
c.imshow("dialated_img",dialated_img)
c.imshow("eroded_img",eroded_img)
c.waitKey(0)

