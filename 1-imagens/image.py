import cv2
 
# Lê a imagem.
# A constante passada no segundo parâmetro define a escala de cor a ser usada:
# cv2.IMREAD_COLOR: Carrega a imagem colorida sem canal alfa (transparência)
# cv.IMREAD_GRAYSCALE: Carrega a imagem em escala de cinza
# cv.IMREAD_UNCHANGED: Carrega a imagem por completo, incluindo o canal alfa
img = cv2.imread("elephant.jpg", cv2.IMREAD_GRAYSCALE)

# Imprime o tamanho da imagem, uma tupla (altura, largura)
print(img.shape)

# Redimensiona a imagem em 50%
resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

# Mostra a imagem redimensionada
cv2.imshow("Elephant", resized_image)

# Salva a nova imagem redimensionada e em escala de cinza
cv2.imwrite('Elephant-grey.jpg', resized_image)

# Espera pelo pressionamento de uma tecla qualquer
key = cv2.waitKey(0) 

# Destrói todas as janelas criadas (nesse caso, só uma)
cv2.destroyAllWindows()