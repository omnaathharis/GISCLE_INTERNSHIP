# import image,show and save.
import cv2
img=cv2.imread("Novak.jpg",1)
cv2.imshow("display",img)
cv2.imwrite("Result.jpg",img)

