#pip install opencv-python

import cv2

#Get the image location and the file name
img_location = "C:/Users/CS"

filename = "smartwatch.jpg"

#Read in the image
img = cv2.imread(img_location + filename)

# Convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
