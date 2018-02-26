import numpy as n
import cv2
img=cv2.imread("novak.jpg",1)
img_gray=cv2.imread("novak.jpg",0)
cv2.imshow("gray",img_gray)
cv2.imwrite("gray.png",img_gray)
Blue=img[100,100,0]
green=img[100,100,1]
red=img[100,100,2]
img[100,100]=[35,46,23]
img.itemset((100,100,0),70)
img.itemset((100,100,1),25)
img.itemset((100,100,2),50)
rows,columns,channels=img.shape
dimension=img.shape
print("pixel value",Blue)
print("pixel value",green)
print("pixel value",red)
print("modified value",img[100,100])
print ("pixel value blue",img[100,100,0])
print ("pixel value green",img[100,100,1])
print ("pixel value red",img[100,100,2])
print("dimension",dimension)
print("rows",rows)
print("columns",columns)
print("channels",channels)
