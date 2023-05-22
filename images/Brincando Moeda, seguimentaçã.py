from PIL import Image

def segmentar_moedas(imagem):
    # Abrir a imagem
    img = Image.open("moeda.jpeg")

    # Converter a imagem para o modo RGB
    img_rgb = img.convert("RGB")

    # Definir os valores de cor para segmentação (intervalo de cor da moeda)
    cor_moeda = (255, 255, 0)  # Cor amarela

    # Criar uma nova imagem para armazenar as moedas segmentadas
    img_segmentada = Image.new("RGB", img.size)

    # Iterar por cada pixel da imagem
    for x in range(img.width):
        for y in range(img.height):
            # Obter o valor RGB do pixel atual
            pixel = img_rgb.getpixel((x, y))

            # Verificar se o pixel está próximo da cor da moeda
            if abs(pixel[0] - cor_moeda[0]) < 30 and abs(pixel[1] - cor_moeda[1]) < 30 and abs(pixel[2] - cor_moeda[2]) < 30:
                # Definir o pixel na imagem segmentada com a cor original
                img_segmentada.putpixel((x, y), pixel)

    # Salvar a imagem segmentada
    img_segmentada.save("moedas_segmentadas.jpg")

    # Exibir a imagem segmentada
    img_segmentada.show()

# Exemplo de uso
imagem = "moedas.jpg"
segmentar_moedas(imagem)
