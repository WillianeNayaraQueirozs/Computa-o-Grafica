from PIL import Image

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Converter a imagem para o modo "RGB"
imagem = imagem.convert("RGB")

# Separar os canais de cores
canal_r, canal_g, canal_b = imagem.split()

# Mostrar os canais separados
canal_r.show()
canal_g.show()
canal_b.show()
