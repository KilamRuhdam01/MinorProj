import cv2
import numpy as np

img = cv2.imread("lena.jpg")

print(img.shape)

imgResize = cv2.resize(img,(640,480))  #width, height
print(imgResize.shape)

imgCropped = imgResize[0:200,200:500]

cv2.imshow("image",imgResize)
cv2.imshow("crop",imgCropped)
cv2.waitKey(0)
