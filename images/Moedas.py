import cv2

def detectar_moedas(imagem):
    # Carregar a imagem
    img = cv2.imread("moeda.jpeg")

    # Redimensionar a imagem para melhor desempenho
    img = cv2.resize(img, (800, 600))

    # Converter a imagem para tons de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar a suavização para reduzir o ruído
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aplicar a detecção de bordas com Canny
    edges = cv2.Canny(blurred, 30, 150)

    # Aplicar a transformada de Hough para detectar círculos
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=50, param2=30, minRadius=10, maxRadius=50)

    # Verificar se foram encontrados círculos
    if circles is not None:
        # Converter as coordenadas e raio para inteiros
        circles = circles.round().astype(int)

        # Contar o número de moedas encontradas
        num_moedas = len(circles[0])

        # Desenhar os círculos na imagem original
        for (x, y, r) in circles[0]:
            cv2.circle(img, (x, y), r, (0, 255, 0), 2)

        # Mostrar a imagem com as moedas detectadas
        cv2.imshow("Moedas Detectadas", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return num_moedas

    else:
        print("Nenhuma moeda encontrada.")
        return 0

# Exemplo de uso
imagem = "moedas.jpg"
num_moedas = detectar_moedas(imagem)
print(f"O número de moedas na imagem é: {num_moedas}")
