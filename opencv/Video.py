# play video from file in normal speed and write it into a file 
import cv2
cap = cv2.VideoCapture('TEST.mp4') # cap = cv2.VideoCapture(0) for webcam capture
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('RESULT.avi', fourcc, 100, (int(cap.get(3)), int(cap.get(4))), isColor=True)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        rgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(rgb)
        cv2.imshow('frame',rgb)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break             

cap.release()
cv2.destroyAllWindows()
