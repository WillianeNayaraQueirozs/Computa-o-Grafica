from PIL import Image

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Separar os canais de cores
canal_r, canal_g, canal_b = imagem.split()

# Criar imagens separadas para cada canal
imagem_r = Image.new("L", imagem.size)
imagem_r.putdata(canal_r.getdata())

imagem_g = Image.new("L", imagem.size)
imagem_g.putdata(canal_g.getdata())

imagem_b = Image.new("L", imagem.size)
imagem_b.putdata(canal_b.getdata())

# Mostrar as imagens dos canais separados
imagem_r.show()
imagem_g.show()
imagem_b.show()
