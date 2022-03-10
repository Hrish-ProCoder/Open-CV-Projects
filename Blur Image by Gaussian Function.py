import cv2

img = cv2.imread('smartwatch.jpg')

avging = cv2.blur(img,(12,12))
