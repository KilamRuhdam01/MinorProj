import cv2
import numpy as np
# cap = cv2.VideoCapture("umcp.mpg")
# while True:
#     success, img = cap.read()
#     cv2.imshow("video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
cap = cv2.VideoCapture(0)
cap.set(3,640)      #width
cap.set(4,480)      #height
cap.set(10,100)    #sets the brightness

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# img = cv2.imread("lena.jpg")
# kernel = np.ones((5,5),np.uint8)

# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny = cv2.Canny(img,200,150)
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=5)
# imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dialated Image", imgDialation)
# cv2.imshow("Erosion Image", imgEroded)
# cv2.waitKey(0)
