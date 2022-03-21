# Import cv2 and numpy
import cv2
import numpy as np

dest = r'C:\Download\watch.jpg'

# Reading an Image
image = cv2.imread(dest)

# Window name in which Image is displayed
window_name = 'Image'

kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernel)
