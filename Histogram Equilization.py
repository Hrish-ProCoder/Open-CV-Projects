import cv2
import numpy as np

image = cv2.imread('C:/HK/Downloads/watch.jpg', 0)

equ = cv2.equalizeHist(img)

res = np.hstack((image, equ))

cv2.imshow(\'img\', res)

cv2.waitKey(0)
