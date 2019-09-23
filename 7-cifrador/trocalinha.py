import cv2
import numpy as np

img = cv2.imread('gato.png')
cifra = "abacate"
i = 0
kernel = np.ones(img.shape, np.float32)

for lin in range(img.shape[0]):
  outra = img.shape[0] - 1 - lin
  # img[lin], img[outra] = img[outra], img[lin]
  kernel[outra] = img[lin]

cv2.imwrite('imagemd.png', kernel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()