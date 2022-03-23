import matplotlib.pyplot as plt
img = plt.imread('watch.jpg')

plt.hist(n_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])


img = cv2.imread('ex.jpg',0)
