import cv2
import sys
import numpy
import random

arquivo = sys.argv[1]
try:
  fatia = int(sys.argv[2])
except IndexError:
  fatia = 15

img = cv2.imread(arquivo)

largura = img.shape[1]
altura = img.shape[0]
beira = largura % fatia
novo_tam = largura - beira
qtd = int(novo_tam / fatia)
nova_img = img[0:altura, 0:novo_tam]
fatias = []

for i in range(qtd):
  f = nova_img[0:altura, 0:fatia]
  nova_img = nova_img[0:altura, fatia:]
  fatias.append(f)

fatiada = numpy.ndarray((altura, novo_tam, 3), numpy.uint8)
pos = 0

random.shuffle(fatias)

for f in fatias:
  fatiada[0:altura, pos:pos+fatia] = f
  pos = pos + fatia

cv2.imwrite("fatiada.png", fatiada)