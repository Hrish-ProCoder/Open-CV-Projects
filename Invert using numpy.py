import cv2
import numpy as np

image = cv2.imread("watch.png", 0)
inverted_image = np.invert(image)
cv2.imwrite("inverted.jpg", inverted)
cv2.imshow("Original Image",image)
