import cv2
import sys
import numpy as np

caminho = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

original = cv2.imread(caminho)
img = cv2.resize(
  original, 
  (int(original.shape[1]/3), int(original.shape[0]/3))
)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
  cinza,
  scaleFactor=1.07,
  minNeighbors=5,
  minSize=(20, 20),
  flags=cv2.CASCADE_SCALE_IMAGE
)

print("Faces encontradas:", len(faces))

kernel = np.ones((7, 7), np.float32) / 25

for (x, y, w, h) in faces:
  # transformar as faces para escala de cinza
  # regiao = img[y:y+h, x:x+w]
  # cinza_1ch = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
  # cinza_3ch = cv2.cvtColor(cinza_1ch, cv2.COLOR_GRAY2BGR)
  # img[y:y+h, x:x+w] = cinza_3ch

  regiao = img[y:y+h, x:x+w]
  borrada = cv2.blur(regiao, (25, 25))
  img[y:y+h, x:x+w] = borrada

# cv2.imshow("Faces", img)
# cv2.waitKey(0)
cv2.imwrite("faces-" + caminho, img)
cv2.destroyAllWindows()