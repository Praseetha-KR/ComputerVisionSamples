import cv2
import numpy as np

img = cv2.imread('media/img.jpg')

px = img[350, 210]
print "at [350, 210], pixel = %s" % (px)

blue = img[350, 210, 0]
green = img[350, 210, 1]
red = img[350, 210, 2]
print "B = %d, G = %d, R = %d" % (blue, green, red)
print img.shape
print 'size = %s' % (img.size)
print 'dtype = %s' % (img.dtype)
for i in range(0, 10):
    for j in range(0, 10):
        img[350 + i, 210 + j] = [255, 255, 255]
        img.itemset((350 + i, 210 + j, 2), 100)

mango = img[280:150, 390:250]
img[0:0, 110:100] = mango

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print img.item(10,10,2)

cv2.destroyAllWindows()

