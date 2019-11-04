import cv2
import sys

arquivo = sys.argv[1]
img = cv2.imread(arquivo, cv2.IMREAD_GRAYSCALE)

largura = img.shape[1]
altura = img.shape[0]

meio = int(largura/2)
dife, seme = 0, 0

print(meio, meio + 1)
for i in range(altura):
  p1 = img[i, meio - 1]
  p2 = img[i, meio]
  dif = abs(int(p1) - int(p2))

  if dif > 80:
    dife += 1
  else:
    seme += 1

porc = seme / altura
print("dif:", dife, "sem:", seme, "taxa:", porc)