import cv2

img = cv2.imread('smartwatch.jpg')

aveging = cv2.blur(img,(12,12))

cv2.imshow('Averaging',aveging)
cv2.waitKey(0)

# Gaussian Blurring

gausBlur = cv2.GaussianBlur(img, (6,6),0)
