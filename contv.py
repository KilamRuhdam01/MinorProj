import numpy as np
import cv2
from PIL import Image as im
from matplotlib import pyplot as plt
from numpy.core.defchararray import asarray

# Create the image as given in the paper

imgArray = np.zeros((8,8), np.uint8)
imgArray[2,1],imgArray[3,1], imgArray[1:5,2], imgArray[2,3], imgArray[2,4], imgArray[1:5,5],imgArray[2:4,6] = 1,1,1,1,1,1,1
print(imgArray)
print(np.shape(imgArray))

# displaying image as a picture
imgPic = im.fromarray(imgArray)
imgPic.save("Img_Bin.png")
im_arr = im.open("Img_Bin.png")
#checking whether the image has been saved properly or not
imarr = asarray(im_arr)
print(imarr)
plt.imshow(imgPic, cmap="gray")
plt.show()

## finding contours using suzukis algorithm
def find_contour_suzuki(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #draw the contours 

    image_cont = cv2.drawContours(img,contours,-1,(0,255,0),2)

    plt.imshow(image_cont)
    plt.show()


find_contour_suzuki(imarr)
#creating a new numpy array for storing adjacency of pixels

def create_adj(i,conn):
    # 'i' gives the number of pixels i.e. one dimesion of the matrix
    array = np.empty((i,i), np.uint8)

    # create adjacency as per the number conn

    if conn ==4 : 
        for rcount in range(i):
            if i == 0 : 
                for ccount in range(i):
                    array[rcount,ccount] = 1
                    array[rcount]





