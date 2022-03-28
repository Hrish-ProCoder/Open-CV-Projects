import cv2

dest = r'C:\Users\HK\Download\watch.jpg'

src = cv2.imread(dest)

window_name = 'Image'

# rotate by 90 degrees clockwise
image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imshow(window_name, image)
cv2.waitKey(0)

# rotate by 180 degrees clockwise
import cv2
dest = r'C:\Users\HK\Download\watch.jpg'
src = cv2.imread(dest)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)
