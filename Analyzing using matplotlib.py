# find histogram of an image
import cv2
from matplotlib import pyplot as plt
image = cv2.imread('watch.jpg',0)

histo = cv2.calcHist([image],[0],None,[256],[0,256])

plt.plot(histo)

plt.show()



# alternate way

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('ex.jpg',0)
