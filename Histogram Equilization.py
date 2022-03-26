import cv2
import numpy as np

image = cv2.imread('C:/HK/Downloads/watch.jpg', 0)

equ = cv2.equalizeHist(image)

res = np.hstack((img, equ))

