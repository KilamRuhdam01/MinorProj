import cv2
import numpy as np

widthImg = 640
heightImg = 480

cap = cv2.VideoCapture(0)
cap.set(3,640)      #width
cap.set(4,480)      #height
cap.set(10,100)    #sets the brightness

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThreshold = cv2.erode(imgDial,kernel,iterations=1)
    return imgThreshold

def getcontours(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours : 
        area = cv2.contourArea(cnt)
        
        
        if area > 5000:
            
            cv2.drawContours(imgContours,cnt,-1,(0,255,0),1)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area >maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    return biggest

def getWarp(img,biggest):
    pass

while True:
    success, img = cap.read()
    cv2.resize(img,(widthImg,heightImg))
    imgContours = img.copy()
    imgThres = preProcessing(img)
    biggest = getcontours(imgThres)
    print(biggest)
    getWarp(img,biggest)
    cv2.imshow("result", imgContours)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

