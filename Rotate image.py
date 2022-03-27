import cv2

dest = r'C:\Users\HK\Download\watch.jpg'

src = cv2.imread(dest)

window_name = 'Image'

# rotate by 90 degrees clockwise
image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
