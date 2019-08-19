import cv2
import numpy as np

def draw_circle(event, x, y, flags, params):
  if event == cv2.EVENT_LBUTTONDBLCLK:
    cv2.circle(img, (x, y), 50, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
  for lin in range(100):
    for col in range(100):
      b, g, r = img[lin, col]    
      img[lin, col] = b + 5, g + 5, r + 5
  cv2.imshow('image', img)
  # val = cv2.waitKey(20)
  # print(val)
  if cv2.waitKey(20) == 27:
    break

cv2.destroyAllWindows()
