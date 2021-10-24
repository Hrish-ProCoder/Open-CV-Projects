# import opencv
import cv2

# Location of Image
# Read in the image
image = cv2.imread('C:\\Documents\\full_path\\tomatoes.jpg')

# Show the image
cv2.imshow('Original', image)
cv2.waitKey(0)
