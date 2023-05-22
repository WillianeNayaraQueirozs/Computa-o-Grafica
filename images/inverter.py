from PIL import Image

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Inverter a imagem horizontalmente
imagem_invertida_horizontalmente = imagem.transpose(Image.FLIP_LEFT_RIGHT)

# Inverter a imagem verticalmente
imagem_invertida_verticalmente = imagem.transpose(Image.FLIP_TOP_BOTTOM)

# Mostrar as imagens invertidas
imagem_invertida_horizontalmente.show()
imagem_invertida_verticalmente.show()
