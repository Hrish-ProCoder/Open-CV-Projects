import cv2

img1 = cv2.imread('cat.jpg')
img2 = cv2.imread('dog.jpg')

im_v = cv2.vconcat([img1, img1])
