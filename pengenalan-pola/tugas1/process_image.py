from tkinter.tix import MAIN
import cv2 
import numpy as np 


MAIN_PATH = "assets/"
#read image
img = cv2.imread(MAIN_PATH + "pokat.jpg")
#check the image shape (width, height, channel)
print (img.shape)
#resize image 
img = cv2.resize(img, (100, 100))
#reshape image into single one-hot encoded 
img_onehot = img.reshape((3 *100 *100, 1))
#encode image to jpg 
img_jpg = cv2.imencode('jpg', img)

#convert to grayscal 
img_gray = cv2.cvtColor(img, "cv2.COLOR_BGR2GRAY")
#crop image to width=20 height=10
img_gray_crop = img_gray[:20, :10]
#save image
cv2.imwrite(img_gray, MAIN_PATH + "gray.jpg")