import cv2

img = cv2.imread('watch.jpg')

blur_image = cv2.blur(img,(21,21))
