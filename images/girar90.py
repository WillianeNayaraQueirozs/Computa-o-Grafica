from PIL import Image

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Girar a imagem em 90 graus
imagem_girada = imagem.rotate(90)

# Mostrar a imagem girada
imagem_girada.show()
