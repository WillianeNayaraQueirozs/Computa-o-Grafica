from PIL import Image, ImageFilter

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Aplicar o filtro da mediana com tamanho de janela de 3x3
imagem_suavizada = imagem.filter(ImageFilter.MedianFilter(size=3))

# Mostrar a imagem suavizada
imagem_suavizada.show()
