import cv2
import sys

caminho = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread(caminho)
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
  cinza,
  scaleFactor=1.1,
  minNeighbors=5,
  minSize=(50, 50),
  flags=cv2.CASCADE_SCALE_IMAGE
)

print("Faces encontradas:", len(faces))