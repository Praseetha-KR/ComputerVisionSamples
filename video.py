import numpy as np
import cv2

cap = cv2.VideoCapture('media/video_test.avi')
# video.avi copyrighted to http://www.mysticfractal.com/video/fractogene.avi

while(cap.isOpened()):
    ret, frame = cap.read()

    if(ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
    else:
        break

if cv2.waitKey(2000) & 0xFF == ord('q'):
    cap.release()
    cv2.destroyAllWindows()
