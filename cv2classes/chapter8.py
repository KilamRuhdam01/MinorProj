import cv2
import numpy as np

def getcontours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours : 
        area = cv2.contourArea(cnt)
        
        
        if area > 500:
            print(area)
            cv2.drawContours(imgcontour,cnt,-1,(0,255,0),1)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objcor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objcor == 3: objectType = "Tri" 
            elif objcor == 4:
                aspectratio = w/float(h)
                if aspectratio >0.95 and aspectratio <1.05: objectType = "Sq"
                else : objectType = "Rect"
            elif objcor >4:
                objectType = "Cir"
            else: objectType = "None"
            cv2.rectangle(imgcontour,(x,y),(x+w,y+h), (10,200,0), 3)
            cv2.putText(imgcontour,objectType,(x+(w//2) - 10, y +(h//2) -10),cv2.FONT_HERSHEY_DUPLEX,0.5,(0,255,0),2)



img = cv2.imread("shape.png")
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggray,(7,7),1)
imgcanny = cv2.Canny(imgblur,100,100)
imgcontour = imggray.copy()
imgblank = np.zeros_like(imggray)
getcontours(imgcanny)
horstack = np.hstack((imgcanny,imggray,imgblur,imgcontour,imgblank))



cv2.imshow("Stack",horstack)

cv2.waitKey(0) 