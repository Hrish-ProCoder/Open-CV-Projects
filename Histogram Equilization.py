import cv2
import numpy as np

image = cv2.imread('C:/HK/Downloads/watch.jpg', 0)

equ = cv2.equalizeHist(img)

# Side by side stacking of img
res = np.hstack((image, equ))

cv2.imshow(\'img\', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
