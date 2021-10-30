import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Desktop/dog.jpg", 1)

# Loading the image
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))
stretch_near = cv2.resize(image, (780, 540), interpolation = cv2.INTER_NEAREST)

Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
