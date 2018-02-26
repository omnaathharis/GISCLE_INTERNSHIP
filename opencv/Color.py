#waitkey,color conversion
import cv2 as c
img=c.imread("novak.jpg",1)
c.imshow("Display",img)
HSV=c.cvtColor(img,c.COLOR_BGR2HSV) # GRAY= c.cvtColor(img,c.COLOR_BGR2GRAY),RGB=c.cvtColor(img,c.COLOR_BGR2RGB)
c.imshow("HSVCONVERSION",HSV)
k=c.waitKey(0) & 0xFF
if k==27:
    c.destroyAllWindows()
elif k ==ord('f'):
    c.imwrite("result2.jpg",HSV)
    c.destroyAllWindows()
