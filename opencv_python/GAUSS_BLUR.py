import cv2
import numpy as np
img=cv2.imread("images.jpg")
gaussianBlur = cv2.GaussianBlur(img,(5,5),1)
cv2.imshow("Gaussian Blur",gaussianBlur)
cv2.imwrite("guassian_blur.png",gaussianBlur)
cv2.waitKey(0)
cv2.destroyAllWindows()
