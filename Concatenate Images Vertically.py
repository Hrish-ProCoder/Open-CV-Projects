# import cv2 library
import cv2

# read the images
img1 = cv2.imread('dog.jpg')
img2 = cv2.imread('cat.jpg')

# cv2.vconcat() used to combine images of same width vertically
img_vrti = cv2.vconcat([img1, img2])

# show the output image
cv2.imshow('pet_img.jpg', img_vrti)
