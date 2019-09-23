import cv2
import numpy as np

imgbg = cv2.imread('gato.png') # background
imgfg = cv2.imread('extintor.png') # foreground

linhas, colunas, canais = imgfg.shape # (linhas, colunas, canais)
roi = imgbg[0:linhas, 0:colunas]

imgfgGray = cv2.cvtColor(imgfg, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(imgfgGray, 120, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

imgbg2 = cv2.bitwise_and(roi, roi, mask = mask_inv)
imgfg2 = cv2.bitwise_and(imgfg, imgfg, mask = mask)

resultado = cv2.add(imgbg2, imgfg2)
imgbg[0:linhas, 0:colunas] = resultado 
cv2.imshow("mascara", imgbg)

cv2.waitKey(0)
cv2.destroyAllWindows()