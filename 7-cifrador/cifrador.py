import cv2
import numpy as np

img = cv2.imread('imagemc.png')
cifra = "abacate"
i = 0

for lin in range(img.shape[0]):
  for col in range(img.shape[1]):
    valueB = img[lin, col, 0] ^ ord(cifra[i])
    valueG = img[lin, col, 1] ^ ord(cifra[i])
    valueR = img[lin, col, 2] ^ ord(cifra[i])

    img[lin, col] = [valueB, valueG, valueR]

    if i < len(cifra) - 1:
      i = i + 1
    else:
      i = 0

cv2.imwrite('imagemd.png', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()