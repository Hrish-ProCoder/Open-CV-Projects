import cv2

img = cv2.imread('smartwatch.png')

avging = cv2.blur(img,(21,21))

cv2.imshow('Averaging',avging)
cv2.waitKey(0)

