# Using cv2.border_constant
import cv2
dest = r'C:\Users\Hrishabh\Downloads\watch.png'
  
image = cv2.imread(path)
window_name = 'Image'
 
# Using cv2.copyMakeBorder() method
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0)
 
cv2.imshow(window_name, image)


# 2nd Method
# Using cv2.border_reflect

image = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT)
