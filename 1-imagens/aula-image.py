import cv2

img = cv2.imread("elephant.jpg", cv2.IMREAD_GRAYSCALE)
print("Altura:", img.shape[0])
print("Largura:", img.shape[1])

a = int(img.shape[0]/2)
l = int(img.shape[1]/2)

print("Novas dimensões:", l, "x", a)

new_img = cv2.resize(img, (l, a))

cv2.imwrite("elephant-cinza.jpg", new_img)

cv2.imshow("Elefante", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()