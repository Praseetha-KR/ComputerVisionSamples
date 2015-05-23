import numpy as np
import cv2

x = np.uint8([250]) # 250 + 10 = 260 => 255     --> Saturated operation
y = np.uint8([10])  # 250 + 10 = 260 % 256 = 4  --> Module operation
print cv2.add(x,y)
print x+y

img1 = cv2.imread('media/img.jpg')
img2 = cv2.imread('media/test_img1.jpg')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

