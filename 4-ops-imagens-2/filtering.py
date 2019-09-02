import cv2
import numpy as np

img = cv2.imread('elephant-cinza.jpg')

kernel = np.ones((5,5),np.float32)/25
region = img[100:150, 100:150]
dst = cv2.filter2D(region,-1,kernel)
img[100:150, 100:150] = dst

cv2.imwrite('teste.jpg', img)