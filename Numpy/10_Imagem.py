
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Abre a imagem
img = Image.open("imagem2.png").convert("RGB")

# Converte a imagem para um array NumPy
array_img = np.array(img)

print("\nFormato do array:")
print(array_img.shape)

# Obtendo as dimensões
altura, largura, canais = array_img.shape

print(f"\nAltura: {altura}")
print(f"Largura: {largura}")
print(f"Canais: {canais}")

# Separando os canais de cores
R = array_img[:, :, 0]  # Vermelho
G = array_img[:, :, 1]  # Verde
B = array_img[:, :, 2]  # Azul

# Coordenadas do pixel que queremos consultar
y_pixel = 590
x_pixel = 1287

# Verifica se o pixel existe na imagem
if y_pixel < altura and x_pixel < largura:
    pixel = array_img[y_pixel, x_pixel]
    r, g, b = pixel

    print(f"\nPixel [{y_pixel}, {x_pixel}]:")
    print(f"R = {r}, G = {g}, B = {b}")
else:
    print("\nA imagem não possui esse pixel.")
    print("Verifique as dimensões da imagem.")

# Define o tamanho do recorte central
recorte_h = 280
recorte_w = 400

# Calcula o centro da imagem
centro_y = altura // 2
centro_x = largura // 2

# Calcula os limites do recorte
y_inicio = centro_y - recorte_h // 2
y_fim = centro_y + recorte_h // 2

x_inicio = centro_x - recorte_w // 2
x_fim = centro_x + recorte_w // 2

# Realiza o recorte
corte_central = array_img[
    y_inicio:y_fim,
    x_inicio:x_fim
]

print(f"\nFormato do recorte: {corte_central.shape}")

# Mostra a imagem original e o recorte central
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Imagem Original")
plt.imshow(array_img)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Corte Central")
plt.imshow(corte_central)
plt.axis("off")

plt.tight_layout()

# Salva o resultado em um arquivo
plt.savefig("resultado.png", dpi=150, bbox_inches="tight")

# Exibe as imagens na tela
plt.show()

# Abrir o terminal no pasta do projeto e usar o comando python 10_Imagem.py