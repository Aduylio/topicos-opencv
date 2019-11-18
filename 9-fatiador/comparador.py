import cv2
import sys
import numpy

arquivo = sys.argv[1]
tam = int(sys.argv[2])
original = cv2.imread(arquivo, cv2.IMREAD_UNCHANGED)
img = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)

largura = img.shape[1]
altura = img.shape[0]

def eh_vizinho(f1, f2, ltr=True, threshold=80):
  dife, seme = 0, 0
  for i in range(altura):
    if ltr:
      p1 = f1[i, -1]
      p2 = f2[i, 0]
    else:
      p1 = f1[i, 0]
      p2 = f2[i, -1]
    dif = abs(int(p1) - int(p2))

    if dif > threshold:
      dife += 1
    else:
      seme += 1

  return seme / altura

fatias = int(largura / tam)
neighbors = []

for j in range(fatias):
  f1 = j * tam
  fat1 = img[0:altura, f1:f1 + tam]
  sim = 0
  nei = -1

  for i in range(fatias):
    f2 = i * tam
    if f1 == f2:
      continue

    fat2 = img[0:altura, f2:f2 + tam]
    porc = eh_vizinho(fat1, fat2, ltr=True, threshold=100)
    tick = "<-" if porc > 0.85 else ""
    if porc > 0.85:
      if porc > sim:
        sim = porc
        nei = i
    
    print("[%d-%d](%d) and [%d-%d](%d): %.2f" % (f1, f1 + tam, j, f2, f2 + tam, i, porc))

  neighbors.append((j, nei))
  print("------------------------")

print("ordenando fatias...")
print("neighbors:", neighbors)
last = -1
ordered = []
while len(neighbors) > len(ordered):
  print("len 1:", len(neighbors), "len 2:", len(ordered))
  for elm in neighbors:
    if elm[1] == last:
      ordered.append(elm)
      last = elm[0]

nova = numpy.ndarray((altura, largura, 3), numpy.uint8)

atual = 0

print("montando...")

while len(ordered) > 0:
  e = ordered.pop()
  print(e[0] * tam, "-", e[0] * tam + tam, "->", atual, "-", atual + tam)

  nova[0:altura, atual:atual + tam] = original[0:altura, e[0] * tam:e[0] * tam + tam]
  atual = atual + tam

cv2.imwrite("montada.png", nova)