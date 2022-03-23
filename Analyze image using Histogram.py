import matplotlib.pyplot as plt
img = plt.imread('watch.jpg')

plt.hist(n_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')

cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# Eg 0-256
img = cv2.imread('smrt.jpg',0)

histg = cv2.calcHist([img],[0],None,[256],[0,256])
