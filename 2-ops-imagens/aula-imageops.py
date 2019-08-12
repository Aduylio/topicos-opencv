import cv2

img = cv2.imread("elephant.jpg", cv2.IMREAD_COLOR)
px = img[100, 100]

for lin in range(img.shape[0]):
  for col in range(img.shape[1]):
    r = min(img[lin, col, 2], 255)
    g = min(img[lin, col, 1], 255)
    b = min(img[lin, col, 0]+ 20, 255)

    img[lin, col] = [b, g, r]

cv2.imshow("Elefante", img)
cv2.waitKey(0)
cv2.destroyAllWindows()