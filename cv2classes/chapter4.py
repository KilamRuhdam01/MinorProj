import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img.shape)
#img[200:300,100:300] = 255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0), thickness=2)
cv2.rectangle(img,(0,0), (500,500),(212,21,255), thickness=2)
cv2.circle(img,(200,200),40,(255,45,34),thickness=4)
cv2.putText(img," OpenCV",(300,200),cv2.FONT_HERSHEY_PLAIN,2,(150,0,45),thickness=2)

cv2.imshow("image", img)

cv2.waitKey(0)