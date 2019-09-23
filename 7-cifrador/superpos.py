import cv2
import numpy as np

cat = cv2.imread('gato.png')
glasses = cv2.imread('logoif.png')

# create a ROI
rows, cols, channels = glasses.shape
roi = cat[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(glasses, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
cv2.imwrite("mask.png", mask_inv)
cv2.imwrite("maskinv.png", mask_inv)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
cv2.imwrite("im1bg.png", img1_bg)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(glasses, glasses, mask = mask)
cv2.imwrite("im2fg.png", img2_fg)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
cat[0:rows, 0:cols ] = dst

cv2.imshow('res', cat)
cv2.waitKey(0)
cv2.destroyAllWindows()