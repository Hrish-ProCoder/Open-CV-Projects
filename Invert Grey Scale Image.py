# import opencv
import cv2

# Read the image
# Load the input image
image = cv2.imread('C:\Desktop\car.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# cvtColor() function
# Grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

