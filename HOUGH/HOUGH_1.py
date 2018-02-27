import cv2
import numpy as np
imd=cv2.imread('d.jpg')
imt=cv2.imread('d.jpg',0)



circles = cv2.HoughCircles(imt,cv2.HOUGH_GRADIENT,1,200)

circles = np.round(circles[0, :]).astype("int")
for (x, y, r) in circles:
    # draw the outer circle
    cv2.circle(imd,(x,y),r,(0,0,255),3)
    

cv2.startWindowThread()
cv2.imshow('detected circles',imd)
cv2.imwrite("hough_detect.png",imd)
cv2.waitKey(0)
cv2.destroyAllWindows()
