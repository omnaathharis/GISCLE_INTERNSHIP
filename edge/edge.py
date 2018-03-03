import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture("DATA2.mp4")
fps = 25
capSize = (854,480)
sizee=854,480,3
edge2Vid = np.zeros(sizee,dtype=np.uint8)
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('edge.avi', fourcc, 100, (int(cap.get(3)), int(cap.get(4))), isColor=False)
success = out.open('video_Output/OutputOfEdgeDetection.mp4',fourcc,fps,capSize,True)
switch = '0 : OFF \n1 : ON'
cv2.namedWindow('canny')
cv2.createTrackbar(switch, 'canny', 0, 1, nothing)

cv2.createTrackbar('lower', 'canny', 0, 255, nothing)
cv2.createTrackbar('upper', 'canny', 0, 255, nothing)

while cap.isOpened():
            ret, image_np = cap.read()
            if ret == True:
                image_np = cv2.cvtColor(image_np,cv2.COLOR_BGR2GRAY)
                # get current positions of four trackbars
                lower = cv2.getTrackbarPos('lower', 'canny')
                upper = cv2.getTrackbarPos('upper', 'canny')
                s = cv2.getTrackbarPos(switch, 'canny')
                if s == 0:
                    edges = image_np
                else:
                    edges = cv2.Canny(image_np, lower, upper)
                    #edges2Vid = edges

                #display images
                out.write(edges)    
                cv2.imshow('canny', edges)
                #edges2 = cv2.cvtColor(edges,cv2.COLOR_GRAY2RGB)
                out.write(edges)
                if cv2.waitKey(25) & 0xFF == ord('s'):
                    
                    cv2.destroyAllWindows()
                    
                    break
            else:
                break

cap.release()
out.release()               
cv2.destroyAllWindows()
