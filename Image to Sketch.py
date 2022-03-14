#pip install opencv-python

import cv2

#Get the image location and the file name
img_location = "C:/Users/CS"

filename = "smartwatch.jpg"

#Read in the image
img = cv2.imread(img_location + filename)
