from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import cv2 as c

driver = webdriver.Chrome(r"E:\My projects\Selenium automation\chromedriver")
driver.maximize_window()
driver.get("https://chromedino.com/black/")

cap = c.VideoCapture(0)
def get_Contours(thresh):
    contours,hierarchy = c.findContours(thresh,c.RETR_EXTERNAL,c.CHAIN_APPROX_NONE)
    contour = max(contours, key=lambda x: c.contourArea(x))
    #x, y, w, h = c.boundingRect(contour)
    #c.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0,0), 2)
    hull = c.convexHull(contour)
    area = c.contourArea(hull)
    c.drawContours(crop_image,[contour],-1,(255,0,0),0)
    c.drawContours(crop_image,[hull],-1,(255,0,0),0)
    if area<20000:
        return True
    else:
        return False
        
    
while True:
    success ,img1 = cap.read()
    img = c.resize(img1,(480,320))
    img = np.array(img[:,::-1])
    c.rectangle(img, (200, 50), (450, 300), (0, 0, 255), 0)
    crop_image = img[50:300, 200:450]
    blur = c.GaussianBlur(crop_image, (5,5), 0)

    hsv = c.cvtColor(crop_image, c.COLOR_BGR2HSV)

    mask2 = c.inRange(hsv, np.array([0, 22, 42]), np.array([255, 255, 255]))
    kernel = np.ones((5,5))

    dilation = c.dilate(mask2, kernel, iterations=1)
    erosion = c.erode(dilation, kernel, iterations=1)
    filtered = c.GaussianBlur(erosion, (3,3), 0)
    ret, thresh = c.threshold(filtered, 70 , 255, 0)
    jump=get_Contours(thresh)
    if jump:
        driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    c.imshow("Thresholded", thresh)
    c.imshow("img",img)
    if c.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
c.destroyAllWindows()

