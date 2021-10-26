# Import opencv
import cv2

# 0 specifies read in grayscale mode
img = cv2.imread('C:\Desktop\car.jpg', 0)

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
