import cv2
import numpy as np
imd=cv2.imread('imag.jpg')
imt=cv2.imread('imag.jpg',0)



circles = cv2.HoughCircles(imt,cv2.HOUGH_GRADIENT,1,15,param1=60,param2=70,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(imd,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(imd,(i[0],i[1]),2,(0,0,255),3)

cv2.startWindowThread()
cv2.imshow('detected circles',imd)
cv2.imwrite("hough_detect.png",imd)
cv2.waitKey(0)
cv2.destroyAllWindows()
