#Declarando as listas que serão usadas
listaT = []
listaX = []
listaY = []
coordenadas = []  #Lista com o tempo, x e y de cada linha do txt
velocidaderobo = []

#Pede posição inicial do robô
posicaoXrobo = float(input("Digite a posição inicial do robô no eixo X: "))
posicaoYrobo = float(input("Digite a posição inicial do robô no eixo Y: "))

#Abre o arquivos e lê as linhas
with open("trajetoria.txt", "r+") as arquivo:
  #Para cada linha lida
  for linha in arquivo.readlines():
    linha = linha.replace(",", ".")  #Substitui a vírgula por ponto
    coordenadas = linha.split()  #Divide a linha em três partes
    listaT.append(coordenadas[0])  #Adiciona o tempo na lista
    listaX.append(coordenadas[1])  #Adiciona o X na lista
    listaY.append(coordenadas[2])  #Adiciona o Y na lista

#Print das listas para verificação
print(listaT)
print()
print(listaX)
print()
print(listaY)
print()
print(coordenadas[0], coordenadas[1], coordenadas[2])
print()


#Função que calcula a velocidade do robô
def velocidadeRobo(
    posicaoXrobo, posicaoYrobo, listaX,
    listaY):  # usa as lista das posições da bola e a posição do robô
  for i in range(1, len(listaX)):
    velocidadeXrobo = (
        float(listaX[i - 1]) - posicaoXrobo
    ) / 0.02  # pega a posição final, que é a bola e a inicial, que é a posição do robô e divide por 0.02 para obter a velocidade
    velocidadeYrobo = (float(listaY[i - 1]) - posicaoYrobo) / 0.02

    print("Velocidade X do Robo: ", round(velocidadeXrobo, 2))
    print("Velocidade Y do Robo: ", round(velocidadeYrobo, 2))
    print()

velocidadeRobo(posicaoXrobo, posicaoYrobo, listaX, listaY)


def velocidadeBola(listaT, listaX, listaY):
  for i in range(1, len(listaT)):
    velocidadeX = (float(listaX[i]) - float(listaX[i - 1])) / 0.02
    velocidadeY = (float(listaY[i]) - float(listaY[i - 1])) / 0.02
    print("Velocidade X da Bola:", round(velocidadeX))
    print("Velocidade Y da Bola:", round(velocidadeY))
    print()

velocidadeBola(listaT, listaX, listaY)
