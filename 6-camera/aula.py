import cv2

captura = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
  _, frame = captura.read()

  faces = faceCascade.detectMultiScale(
    frame,
    scaleFactor=1.07,
    minNeighbors=5,
    minSize=(20, 20),
    flags=cv2.CASCADE_SCALE_IMAGE
  )

  for (x, y, w, h) in faces:
    regiao = frame[y:y+h, x:x+w]
    borrada = cv2.blur(regiao, (25, 25))
    frame[y:y+h, x:x+w] = borrada

  cv2.imshow("Video", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

captura.release()
cv2.destroyAllWindows()