from PIL import Image, ImageFilter

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Aplicar o filtro da média ponderada com tamanho de janela de 3x3
imagem_suavizada = imagem.filter(ImageFilter.GaussianBlur(3))

# Mostrar a imagem suavizada
imagem_suavizada.show()
