import cv2

image = cv2.imread('images/suco_limao.jpg')
print('Largura em pixels: ', image.shape[1])
"""image.shape[1] o '1' indica a largura"""
print('Altura em pixels: ', image.shape[0])
"""image.shape[2] o '0' indica a altura"""
print('Quantidade de Canais', image.shape[2])
"""image.shape[2] o '2' indica a quantidade de canais que a foto possui"""
"""Lendo largura da imagem"""
cv2.imshow('Suco', image)
"""Nome da tela 'Suco'"""
cv2.waitKey(0)
"""Esperar qualquer tecla para que a tela feche"""
cv2.imwrite("ImagemSalva", image)
