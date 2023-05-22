from PIL import Image, ImageFilter

# Abrir a imagem
imagem = Image.open("barbie.jpg")

# Aplicar o filtro de desfoque gaussiano
imagem_suavizada = imagem.filter(ImageFilter.GaussianBlur(radius=2))

# Mostrar a imagem suavizada
imagem_suavizada.show()
