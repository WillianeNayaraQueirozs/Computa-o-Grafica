from PIL import Image

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Ajustar o brilho
fator_brilho = 1.5  # Valor maior que 1 aumenta o brilho, valor menor que 1 diminui o brilho
imagem_ajustada = imagem.point(lambda p: p * fator_brilho)

# Mostrar a imagem ajustada
imagem_ajustada.show()
