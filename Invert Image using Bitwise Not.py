import cv2
image = cv2.imread("watch.png", 0)

inverted_image = cv2.bitwise_not(image)
cv2.imwrite("inverted.jpg", inverted)

cv2.imshow("Original Image",image)
