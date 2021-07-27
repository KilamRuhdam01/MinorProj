#%% Functions to create image using openCV
#import cv2

import numpy as np


#%% Draw overflowing to the other side V
x=y=16
def imageV():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)                                 #CHANGED FROM (X,Y,1) to (1,x,y) that means one plane of (x,y) dimensions.
    image.fill(255)
    image[15,2,0] = 0  # Set the RGBA Value of the image (tuple)
    image[14,1,0] = 0  # Set the RGBA Value of the image (tuple)
    image[13,0,0] = 0  # Set the RGBA Value of the image (tuple)
    image[12,15,0] = 0  # Set the RGBA Value of the image (tuple)
    image[11,14,0] = 0  # Set the RGBA Value of the image (tuple)
    image[10,13,0] = 0  # Set the RGBA Value of the image (tuple)
    image[9,12,0] = 0  # Set the RGBA Value of the image (tuple)
    image[8,11,0] = 0  # Set the RGBA Value of the image (tuple)
    image[7,12,0] = 0  # Set the RGBA Value of the image (tuple)
    image[6,13,0] = 0  # Set the RGBA Value of the image (tuple)
    image[5,14,0] = 0  # Set the RGBA Value of the image (tuple)
    image[4,15,0] = 0  # Set the RGBA Value of the image (tuple)
    image[3,0,0] = 0  # Set the RGBA Value of the image (tuple)
    image[2,1,0] = 0  # Set the RGBA Value of the image (tuple)
    image[1,2,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[15,1,0] = 0  # Set the RGBA Value of the image (tuple)
    # duplicate the trace to make thicker line
    # image[4,5,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[5,6,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[6,7,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[7,8,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[8,9,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[9,10,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[10,11,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[11,10,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[12,9,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[13,8,0] = 0  # Set the RGBA Value of the image (tuple)
    return image

#%% Draw right opening V with corners right on the edges
def imageV1():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)                                 #CHANGED FROM (X,Y,1) to (1,x,y) that means one plane of (x,y) dimensions.
    image.fill(255)

    # right side opening V
    image[0,15,0] = 0  # Set the RGBA Value of the image (tuple)
    image[1,14,0] = 0  # Set the RGBA Value of the image (tuple)
    image[2,13,0] = 0  # Set the RGBA Value of the image (tuple)
    image[3,12,0] = 0  # Set the RGBA Value of the image (tuple)
    image[4,11,0] = 0  # Set the RGBA Value of the image (tuple)
    image[5,10,0] = 0  # Set the RGBA Value of the image (tuple)
    image[6,9,0] = 0  # Set the RGBA Value of the image (tuple)
    image[7,8,0] = 0  # Set the RGBA Value of the image (tuple)
    image[8,9,0] = 0  # Set the RGBA Value of the image (tuple)
    image[9,10,0] = 0  # Set the RGBA Value of the image (tuple)
    image[10,11,0] = 0  # Set the RGBA Value of the image (tuple)
    image[11,12,0] = 0  # Set the RGBA Value of the image (tuple)
    image[12,13,0] = 0  # Set the RGBA Value of the image (tuple)
    image[13,14,0] = 0  # Set the RGBA Value of the image (tuple)
    image[14,15,0] = 0  # Set the RGBA Value of the image (tuple)

    ## left side opening V
    # image[0,0,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[1,1,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[2,2,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[3,3,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[3,4,0] = 0
    # image[3,5,0] = 0
    # image[3,6,0] = 0
    # image[4,4,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[5,5,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[6,6,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[7,7,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[8,8,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[9,7,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[10,6,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[11,5,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[12,4,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[13,3,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[14,2,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[15,1,0] = 0

    # duplicate the trace to make thicker line
    # image[4,5,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[5,6,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[6,7,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[7,8,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[8,9,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[9,10,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[10,11,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[11,10,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[12,9,0] = 0  # Set the RGBA Value of the image (tuple)
    # image[13,8,0] = 0  # Set the RGBA Value of the image (tuple)
    return image


#%% Draw offset V
def imageV2():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)                                 #CHANGED FROM (X,Y,1) to (1,x,y) that means one plane of (x,y) dimensions.
    image.fill(255)

    ## right side opening V
    
    image[1,13,0] = 0  # Set the RGBA Value of the image (tuple)
    image[2,12,0] = 0  # Set the RGBA Value of the image (tuple)
    image[3,11,0] = 0  # Set the RGBA Value of the image (tuple)
    image[4,10,0] = 0  # Set the RGBA Value of the image (tuple)
    image[5,9,0] = 0  # Set the RGBA Value of the image (tuple)
    image[6,8,0] = 0  # Set the RGBA Value of the image (tuple)
    image[7,9,0] = 0  # Set the RGBA Value of the image (tuple)
    image[8,10,0] = 0  # Set the RGBA Value of the image (tuple)
    image[9,11,0] = 0  # Set the RGBA Value of the image (tuple)
    image[10,12,0] = 0  # Set the RGBA Value of the image (tuple)
    image[11,13,0] = 0  # Set the RGBA Value of the image (tuple)
    image[12,14,0] = 0  # Set the RGBA Value of the image (tuple)
    image[13,15,0] = 0  # Set the RGBA Value of the image (tuple)
    #image[14,15,0] = 0  # Set the RGBA Value of the image (tuple)
    return image

# %% Fill Square
def imageSquare():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)
    image.fill(255)
    for i in range(4,x-4):
        for j in range(4,y-4):
            image[i,j] = 0
    return image

# %% Fill a circle
def imageCircle():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)
    image.fill(255)
    for i in range(x):
        for j in range(y):
            if ((((i-x/2)**2 + (j-x/2)**2) > 30) ):
            #and (((i-x/2)**2 + (j-x/2)**2) < 45)):
                image[i,j] = 0
            # if ((((i-x/2)**2 + (j-y/2)**2) > 300) and (((i-x/2)**2 + (j-y/2)**2) < 450)):
            #     image[i,j] = 0
    return image

#%% Make a cross
def imageCross():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)
    image.fill(255)
    for i in range(4,x-4):
        image[i,i] = 0
        image[i,y-i] = 0
    return image

#%% Make a plus
def imagePlus():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)
    image.fill(255)
    halfx = int(x/2)
    halfy = int(y/2)
    for i in range(4,x-4):
        image[i,halfy] = 0
        image[halfx,i] = 0
    return image

#%% Make a plus
def imageGrid():
    x=y=16
    image = np.zeros((x,y,1), np.uint8)
    image.fill(255)
    for i in range(x):
        for j in range(y):
            if ((i%2 == 1) or (j%2 == 1)):      ## either is odd
                image[i,j] = 0
    return image

#%% Make image 1a from Contour representation of binary images using run-type direction codes
def image1a():
    x = 6
    y = 8
    image = np.zeros((x,y,1), np.uint8)
    image.fill(255)
    image[1,2] = 0  # Set the RGBA Value of the image (tuple)
    image[2,1] = 0  # Set the RGBA Value of the image (tuple)
    image[2,2] = 0  # Set the RGBA Value of the image (tuple)
    image[2,3] = 0  # Set the RGBA Value of the image (tuple)
    image[3,1] = 0  # Set the RGBA Value of the image (tuple)
    image[3,2] = 0  # Set the RGBA Value of the image (tuple)
    image[4,2] = 0  # Set the RGBA Value of the image (tuple)

    image[1,5] = 0  # Set the RGBA Value of the image (tuple)
    image[2,4] = 0  # Set the RGBA Value of the image (tuple)
    image[2,5] = 0  # Set the RGBA Value of the image (tuple)
    image[2,6] = 0  # Set the RGBA Value of the image (tuple)
    image[3,5] = 0  # Set the RGBA Value of the image (tuple)
    image[3,6] = 0  # Set the RGBA Value of the image (tuple)
    image[4,5] = 0  # Set the RGBA Value of the image (tuple)
    return image
