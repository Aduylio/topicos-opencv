import cv2
import sys

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

for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow("Faces", img)
# cv2.waitKey(0)
cv2.imwrite("faces-" + caminho, img)
cv2.destroyAllWindows()