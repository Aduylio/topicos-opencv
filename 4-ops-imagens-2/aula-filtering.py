import cv2
import numpy as np

img = cv2.imread('pavao.jpeg')
regiao = img[60:160, 100:180] # [y1:y2, x1:x2]
cinza = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
cinza_3ch = cv2.cvtColor(cinza, cv2.COLOR_GRAY2BGR)
img[60:160, 100:180] = cinza_3ch

cv2.imshow('imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()