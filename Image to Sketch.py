#pip install opencv-python

import cv2

#Get the image location and the file name
img_location = "C:/Users/CS"

filename = "smartwatch.jpg"

#Read in the image
img = cv2.imread(img_location + filename)

# Convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_gray_image = 255 - gray_image

# Blur the image by gaussian function
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

# Invert blur image
inverted_blurred_image = 255 - blurred_image

# Create the pencil sketch image
pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)

#Show the image
cv2.imshow('Original Image', img)
cv2.imshow('New Image_g', gray_image)
cv2.imshow('New Image_ig', inverted_gray_image)
cv2.imshow('New Image_bi', blurred_image)
cv2.imshow('New Image_ibi', inverted_blurred_image)
cv2.imshow('New Image_finale', pencil_sketch_img)

cv2.waitKey(0)
