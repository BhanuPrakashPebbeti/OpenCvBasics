import cv2 as c

cap = c.VideoCapture("test_video.mp4")

while True:
    success,img = cap.read()
    c.imshow("Video",img)
    if c.waitKey(1)& 0xFF==ord("q"):
        break
cap.release()
c.destroyAllWindows()
