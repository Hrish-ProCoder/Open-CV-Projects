import cv2
import numpy as np

image = cv2.imread("watch.png", 0)
inverted_image = np.invert(image)
