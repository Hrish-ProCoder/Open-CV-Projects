import cv2
import numpy as np

dest = r'C:\Download\watch.jpg'

image = cv2.imread(dest)

window_name = 'Image'

kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)
