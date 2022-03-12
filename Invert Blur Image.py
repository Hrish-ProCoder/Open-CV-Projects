import cv2

img = cv2.imread('watch.jpg')

blur_image = cv2.blur(img,(21,21))
cv2.imshow('blurred image',blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
