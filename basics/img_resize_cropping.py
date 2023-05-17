import cv2 as c

img = c.imread("lena.png")
print(img.shape)

imgresize = c.resize(img,(500,500)) #1000=width,500=height
print(imgresize.shape)              #gives(height,width)

imgcropped = imgresize[0:250,250:500] #(height,width)
c.imshow("image",img)
c.imshow("resized",imgresize)
c.imshow("cropped",imgcropped)
c.waitKey(0)


