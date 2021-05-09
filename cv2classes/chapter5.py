from typing import no_type_check
import cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix

img = cv2.imread("cards.jpg")
width,height = 250,350
print(img.shape)
pts1 = np.float32([[111,219],[287,188],[154,244],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgout = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("out",imgout)
cv2.waitKey(0)