# import opencv
import cv2

# Read the image
# Load the input image
image = cv2.imread('C:\Desktop\car.jpg')

# cvtColor() function
# Greyscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the image
Inverted_grayimage = 255 - gray_image

# Show image
cv2.imshow('Original Image', inverted_gray_image)
cv2.imshow('New Image', inverted_gray_image)
cv2.waitKey(0) 

cv2.destroyAllWindows()
