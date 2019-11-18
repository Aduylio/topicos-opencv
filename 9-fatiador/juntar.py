import cv2
import sys
import numpy

arquivo = sys.argv[1]
tam = int(sys.argv[2])
original = cv2.imread(arquivo, cv2.IMREAD_UNCHANGED)
img = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)

largura = img.shape[1]
altura = img.shape[0]

def eh_vizinho(f1, f2, threshold=80):
  seme = 0
  for linha in range(altura):
    p1 = int(f1[linha, -1]) #uint8
    p2 = int(f2[linha, 0])  #uint8
    dif = abs(p1 - p2)

    if dif <= threshold:
      seme += 1

  return seme / altura

fatias = int(largura / tam)
vizinhos = []

for j in range(fatias):
  f1 = j * tam # onde começa fatia1 
  fat1 = img[0:altura, f1:f1 + tam] # a fatia (imagem)
  maior = 0 # maior percentual de semelhança
  viz = -1 # no fim do próximo for, o vizinho da fatia2

  for i in range(fatias):
    f2 = i * tam # onde começa fatia2
    if f1 == f2:
      continue

    fat2 = img[0:altura, f2:f2 + tam]
    perc = eh_vizinho(fat1, fat2, threshold=90)

    if perc > 0.85:
      if perc > maior:
        maior = perc
        viz = i

  vizinhos.append( (j, viz) )

print("vizinhos:", vizinhos)

ultimo = -1
ordenada = []

while len(vizinhos) > len(ordenada):
  for elm in vizinhos:
    if elm[1] == ultimo:
      ordenada.append(elm)
      ultimo = elm[0]

nova = numpy.ndarray((altura, largura, 3), numpy.uint8)

for atual in range(fatias):
  e = ordenada.pop()
  nova[0:altura, atual:atual + tam] = original[0:altura, e[0] * tam:e[0] * tam + tam]

cv2.imwrite("montada.png", nova)