import  cv2 as c
import numpy as np
 
def empty(a):
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
 
 
path = 'lambo.png'
c.namedWindow("TrackBars")
c.resizeWindow("TrackBars",640,240)
c.createTrackbar("Hue Min","TrackBars",0,179,empty)
c.createTrackbar("Hue Max","TrackBars",19,179,empty)
c.createTrackbar("Sat Min","TrackBars",110,255,empty)
c.createTrackbar("Sat Max","TrackBars",240,255,empty)
c.createTrackbar("Val Min","TrackBars",153,255,empty)
c.createTrackbar("Val Max","TrackBars",255,255,empty)
 
while True:
    img = c.imread(path)
    imgHSV = c.cvtColor(img,c.COLOR_BGR2HSV)
    
    if c.waitKey(1) & 0xFF==ord("q"):
        break
    
    h_min = c.getTrackbarPos("Hue Min","TrackBars")
    h_max = c.getTrackbarPos("Hue Max", "TrackBars")
    s_min = c.getTrackbarPos("Sat Min", "TrackBars")
    s_max = c.getTrackbarPos("Sat Max", "TrackBars")
    v_min = c.getTrackbarPos("Val Min", "TrackBars")
    v_max = c.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = c.inRange(imgHSV,lower,upper)
    imgResult = c.bitwise_and(img,img,mask=mask)
 
 
 
    imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
    c.imshow("Stacked Images", imgStack)
    c.waitKey(1)
c.destroyAllWindows()