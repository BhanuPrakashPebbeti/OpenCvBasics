import cv2 as c

img = c.imread("lena.png")
c.imshow("output",img)
c.waitKey(0)

