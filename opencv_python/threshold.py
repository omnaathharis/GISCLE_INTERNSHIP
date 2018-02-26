import cv2
import numpy as np
def nothing(x):
    pass
image_org = cv2.imread('horse.jpg')
image = cv2.cvtColor(image_org,cv2.COLOR_RGB2HSV)
maxval = 255
thresh=1
type_thresh = 5
cv2.namedWindow("Adjust",cv2.WINDOW_AUTOSIZE);
cv2.createTrackbar("Thresh", "Adjust", thresh, 200, nothing);
cv2.createTrackbar("Max", "Adjust", maxval, 255, nothing);

cv2.createTrackbar("Type", "Adjust", type_thresh, 5, nothing); 

Threshold = np.zeros(image.shape, np.uint8)


while 1:
    thresh = cv2.getTrackbarPos('Thresh', 'Adjust')
    maxval = cv2.getTrackbarPos('Max', 'Adjust')
    type_thresh = cv2.getTrackbarPos('Type', 'Adjust')
    retva,Threshold = cv2.threshold(image,thresh,maxval,type_thresh)
    
    cv2.imshow('Adjust', Threshold)
    cv2.imshow('Original', image_org)
    cv2.imwrite('output.png',Threshold)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   
        break
        
cv2.destroyAllWindows()        
