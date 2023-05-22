from PIL import Image, ImageEnhance

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Ajustar o contraste
fator_contraste = 1.5  # Valor maior que 1 aumenta o contraste, valor menor que 1 diminui o contraste
ajuste_contraste = ImageEnhance.Contrast(imagem)
imagem_ajustada = ajuste_contraste.enhance(fator_contraste)

# Mostrar a imagem ajustada
imagem_ajustada.show()
