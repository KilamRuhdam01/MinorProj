from construct import imageV
import algos

import numpy as np
from PIL import Image as im
import cv2
from matplotlib import pyplot as plt






if __name__ == "__main__" : 
    X = np.reshape(imageV(),(16,16))
    print(X)
    
    imgPic = im.fromarray(X, mode ='L')
    plt.imshow(imgPic, cmap='gray')
    plt.show()


