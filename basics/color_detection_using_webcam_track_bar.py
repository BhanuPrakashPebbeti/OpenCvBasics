import cv2 as c
import numpy as np

def nothing(x):
    pass

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

#cap = c.VideoCapture("http://192.168.43.1:8080/video")
cap = c.VideoCapture(0)
c.namedWindow("TrackBars")
# create trackbars for color change
c.createTrackbar('Hue Min','TrackBars',0,255,nothing)
c.createTrackbar('Hue Max','TrackBars',0,255,nothing)
c.createTrackbar('Sat Min','TrackBars',0,255,nothing)
c.createTrackbar('Sat Max','TrackBars',0,255,nothing)
c.createTrackbar('Val Min','TrackBars',0,255,nothing)
c.createTrackbar('Val Max','TrackBars',0,255,nothing)



while True:
    ret, img1 = cap.read()
    img1 = np.flip(img1,axis=1)
    img = c.resize(img1,(540,360))
    blur = c.GaussianBlur(img, (5,5), 0)
    hsv = c.cvtColor(blur, c.COLOR_BGR2HSV)

    if c.waitKey(1) & 0xFF==ord("q"):
        break
    
    # get current positions of four trackbars
    rl = c.getTrackbarPos('Hue Min','TrackBars')
    rh = c.getTrackbarPos('Hue Max','TrackBars')

    gl = c.getTrackbarPos('Sat Min','TrackBars')
    gh = c.getTrackbarPos('Sat Max','TrackBars')

    bl = c.getTrackbarPos('Val Min','TrackBars')
    bh = c.getTrackbarPos('Val Max','TrackBars')

    lower = np.array([rl,gl,bl])
    upper = np.array([rh,gh,bh])

    print(rl,gl,bl,rh,gh,bh)

    mask = c.inRange(hsv, lower, upper)    
    color_mask = c.bitwise_and(img,img,mask=mask)
    imgStack = stackImages(1,([img,hsv],[mask,color_mask]))

    c.imshow("ImageStack",imgStack)

cap.release()
c.destroyAllWindows()