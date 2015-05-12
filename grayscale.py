import numpy as np
import cv2

img = cv2.imread('media/img.jpg', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:             # ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):     # 's' key to save & exit
    cv2.imwrite('media/gen_img_gray.png', img)
    cv2.destroyAllWindows()

#test
