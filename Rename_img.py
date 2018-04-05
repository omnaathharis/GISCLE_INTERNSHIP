import os
import numpy as np
import cv2 as cv
dire='OUTPUT1'
count=1102
for img in os.listdir(dire):
    f1=cv.imread('OUTPUT1/'+img)
    cv.imwrite("image"+"%d.jpg" % count,f1 )
    count=count+1
 
