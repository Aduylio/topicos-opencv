import cv2
import numpy as np

img = cv2.imread('elephant.jpg', cv2.IMREAD_COLOR)

# Obtém o pixel localizado na coordenada 100, 100
# O pixel é representado por uma lista [ B, G, R ],
# onde B é a intensidade do azul, G do verde e R do vermelho.
px = img[100, 100]
print(px)

# Obtém o valor da intensidade do canal azul do pixel
# Posição:
# 0 - azul
# 1 - verde
# 2 - vermelho
blue = img[100, 100, 0]
print(blue)

# Para modificar um pixel, basta atribuir uma nova lista
# à determinada posição da imagem.
# Aumenta o valor da intensidade de cada cor em 20 em uma
# região da imagem de largura 50 e altura 100 px.
for lin in range(100, 200):
  for col in range(200, 250):
    old = img[lin, lin]
    r = old[2] + 20
    g = old[1] + 20
    b = old[0] + 20
    img[lin, col] = [b, g, r]

region = img[100:200, 150:250]
img[150:200, 200:250] = region

# Salva 
cv2.imwrite('elephant-mod.jpg', img)