import cv2 as c
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = c.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = c.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= c.cvtColor( imgArray[x][y], c.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = c.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = c.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = c.cvtColor(imgArray[x], c.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img1 = c.imread('cards.jpg')
img = c.resize(img1,(200,200))
imgGray = c.cvtColor(img,c.COLOR_BGR2GRAY)

imgStack = stackImages(1,([img,imgGray,img],[img,img,img],[img,img,img]))

c.imshow("ImageStack",imgStack)

c.waitKey(0)