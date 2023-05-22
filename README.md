# Computação Grafica
Filtros de computação Grafica

# Filtro com Pillow

## Requisitos

Python 3.x
Pillow (instalado via pip install pillow)

# Filtros Disponíveis

## Filtro de Separação de Canais RGB

Este filtro separa os canais de cores (vermelho, verde e azul) de uma imagem. Ele converte a imagem para o modo "RGB" e separa os canais utilizando a função split().

## Conversão de Tons de Cinza para Preto e Branco (Limiarização/Binarização Manual)

Este filtro converte uma imagem em tons de cinza para uma imagem em preto e branco utilizando a técnica de limiarização/binarização manual. Ele define um valor de limiar e percorre os pixels da imagem, atribuindo o valor 0 (preto) aos pixels abaixo do limiar e 255 (branco) aos pixels acima do limiar.

## Filtro de Média Simples

Este filtro aplica o filtro da média simples em uma imagem. Ele utiliza o filtro BoxBlur da biblioteca Pillow com um tamanho de janela de 3x3 para realizar a suavização da imagem.

## Filtro de Mediana

Este filtro aplica o filtro da mediana em uma imagem. Ele utiliza o filtro MedianFilter da biblioteca Pillow com um tamanho de janela de 3x3 para realizar a suavização da imagem.

## Filtro de Desfoque Gaussiano

Este filtro aplica o filtro de desfoque gaussiano em uma imagem. Utiliza o filtro GaussianBlur da biblioteca Pillow com um determinado raio para suavizar a imagem.

## Filtro de Ajuste de Brilho

Este filtro ajusta o brilho de uma imagem. É possível aumentar ou diminuir o brilho da imagem utilizando um fator de brilho. Valores maiores que 1 aumentam o brilho, enquanto valores menores que 1 diminuem o brilho.

## Filtro de Ajuste de Contraste

Este filtro ajusta o contraste de uma imagem. É possível aumentar ou diminuir o contraste da imagem utilizando um fator de contraste. Valores maiores que 1 aumentam o contraste, enquanto valores menores que 1 diminuem o contraste.

## Filtro de Rotação de Imagem

Este filtro gira a imagem em um ângulo específico. Utiliza a função rotate() da biblioteca Pillow para girar a imagem em graus definidos.

## Filtro de Inversão de Imagem

Este filtro inverte a imagem horizontalmente e verticalmente. Utiliza as funções transpose() e FLIP_LEFT_RIGHT/FLIP_TOP_BOTTOM da biblioteca Pillow para realizar as inversões.

# Moeda 

## Feito por mim Williane Nayara Queiroz e Ana C. Reis Peres

# Detecção de Moedas

Este código em Python utiliza a biblioteca OpenCV para detectar moedas em uma imagem.

## Funcionamento do Código

O código segue os seguintes passos para detectar as moedas na imagem:

1. Carregar a imagem e redimensioná-la para melhor desempenho.
2. Converter a imagem para tons de cinza.
3. Aplicar uma suavização para reduzir o ruído.
4. Aplicar a detecção de bordas utilizando o algoritmo Canny.
5. Utilizar a transformada de Hough para detectar círculos na imagem.
6. Verificar se foram encontrados círculos.
7. Se círculos foram encontrados, desenhar os círculos na imagem original.
8. Mostrar a imagem com as moedas detectadas.
9. Retornar o número de moedas encontradas.




