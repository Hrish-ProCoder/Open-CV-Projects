import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Desktop/dog.jpg", 1)

# Loading the image
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
