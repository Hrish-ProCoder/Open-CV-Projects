import cv2
img = cv2.imread('watch.png')

avging = cv2.blur(img,(20,20))
