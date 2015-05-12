import numpy as np
import cv2

img = cv2.imread('media/img.jpg', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.imwrite('media/img_gray_gen.png', img)
cv2.destroyAllWindows()
cv2.waitKey(1)
