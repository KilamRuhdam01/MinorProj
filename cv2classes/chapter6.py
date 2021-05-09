import cv2
import numpy as np

img = cv2.imread("lena.jpg")

imghor = np.hstack((img,img))
imgver = np.vstack((img,img))


cv2.imshow("hor",imghor)
cv2.imshow("ver",imgver)

cv2.waitKey(0)
