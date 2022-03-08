import cv2
img = cv2.imread('watch.png')

avging = cv2.blur(img,(20,20))

cv2.imshow('Averaging',avging)
cv2.waitKey(0)

# Median blurring
medBlur = cv2.medianBlur(img,5)
cv2.imshow('Media Blurring', medBlur)

cv2.waitKey(0)
