from PIL import Image, ImageFilter

# Abrir a imagem MEDIA SIMPLES
imagem = Image.open("barbie.jpg")

# Aplicar o filtro da média simples com tamanho de janela de 3x3
imagem_suavizada = imagem.filter(ImageFilter.BoxBlur(3))

# Mostrar a imagem suavizada
imagem_suavizada.show()
