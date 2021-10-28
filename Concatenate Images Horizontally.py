import cv2

img1 = cv2.imread('cat.jpg')
img2 = cv2.imread('dog.jpg')

images = cv2.vconcat([img1, img1])

cv2.imshow('Image.jpg', images)
