from PIL import Image

# Abrir a imagem em tons de cinza
imagem_cinza = Image.open("barbie.jpg")

# Definir um valor de limiar
limiar = 128

# Converter a imagem para o modo "L" (tons de cinza) se necessário
if imagem_cinza.mode != "L":
    imagem_cinza = imagem_cinza.convert("L")

# Obter os pixels da imagem
pixels = imagem_cinza.load()

# Aplicar a limiarização/binarização manual
for i in range(imagem_cinza.width):
    for j in range(imagem_cinza.height):
        if pixels[i, j] < limiar:
            pixels[i, j] = 0  # Preto
        else:
            pixels[i, j] = 255  # Branco

# Mostrar a imagem binarizada
imagem_cinza.show()

