#Declarando as listas que serão usadas
listaT = []
listaX = []
listaY = []
coordenadas = []  #Lista com o tempo, x e y de cada linha do txt

#Listas de velocidade
lista_VelocidadeX_robo = []
lista_VelocidadeY_robo = []
lista_VelocidadeX_bola = []
lista_VelocidadeY_bola = []

#Listas de aceleração
lista_AceleracaoX_robo = []
lista_AceleracaoY_robo = []
lista_AceleracaoX_bola = []
lista_AceleracaoY_bola = []


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

#Print dos pontos para verificação
print(coordenadas[0], coordenadas[1], coordenadas[2])
print()


#Função que calcula a velocidade do robô
def velocidadeRobo(posicaoXrobo, posicaoYrobo, listaX, listaY):  # usa as lista das posições da bola e a posição do robô
  for i in range(1, len(listaX)):
    # pega a posição final, que é a bola e a inicial, que é a posição do robô e divide por 0.02 para obter a velocidade
    velocidadeXrobo = round(((float(listaX[i - 1]) - posicaoXrobo) / 0.02), 3)
    lista_VelocidadeX_robo.append(velocidadeXrobo)
    velocidadeYrobo = round(((float(listaY[i - 1]) - posicaoYrobo) / 0.02), 3)
    lista_VelocidadeY_robo.append(velocidadeYrobo)
    print("Velocidade X do Robo: ", velocidadeXrobo)
    print("Velocidade Y do Robo: ", velocidadeYrobo)
    print()

velocidadeRobo(posicaoXrobo, posicaoYrobo, listaX, listaY)

def velocidadeBola(listaT, listaX, listaY):
  for i in range(1, len(listaT)):
    velocidadeXbola = round(((float(listaX[i]) - float(listaX[i - 1])) / 0.02), 3)
    lista_VelocidadeX_bola.append(velocidadeXbola)
    velocidadeYbola = round(((float(listaY[i]) - float(listaY[i - 1])) / 0.02), 3)
    lista_VelocidadeY_bola.append(velocidadeYbola)
    print("Velocidade X da Bola:", velocidadeXbola)
    print("Velocidade Y da Bola:", velocidadeYbola)
    print()

velocidadeBola(listaT, listaX, listaY)

# função que calcula aceleração da BOLA recebe lista de velocidades em X e em Y e a lista de tempo
def aceleracaoBola(lista_VelocidadeX_bola, lista_VelocidadeY_bola, listaT):
  # usando a lista T para calcular as acelerações
  for i in range(1, len(listaT) - 1):
    # aceleração em X da bola = posição i da lista subtraída da anterior, dividido pelo tempo
    aceleracaoXbola = round(((float(lista_VelocidadeX_bola[i]) - float(lista_VelocidadeX_bola[i - 1])) / 0.02), 3)
    # esse valor será armazenado na lista de aceleração em X da bola para plotagem posterior
    lista_AceleracaoX_bola.append(aceleracaoXbola)
    # mesma coisa para aceleração em Y
    aceleracaoYbola = round(((float(lista_VelocidadeY_bola[i]) - float(lista_VelocidadeY_bola[i - 1])) / 0.02), 3)
    lista_AceleracaoY_bola.append(aceleracaoYbola)
    print("Aceleração X da Bola:", aceleracaoXbola)
    print("Aceleração Y da Bola:", aceleracaoYbola)
    print()

# chama a função
aceleracaoBola(lista_VelocidadeX_bola, lista_VelocidadeY_bola, listaT)


# função que calcula aceleração do ROBO recebe lista de velocidades em X e em Y e a lista de tempo
def aceleracaoRobo(lista_VelocidadeX_robo, lista_VelocidadeY_robo, listaT):
   # usando a lista T para calcular as acelerações
  for i in range(1, len(listaT) - 1):
    # aceleração em X do robo = a posição i da lista subtraída da anterior, dividido pelo tempo
    aceleracaoXrobo = round(((float(lista_VelocidadeX_robo[i]) - float(lista_VelocidadeX_robo[i - 1])) / 0.02), 3)
    # esse valor será armazenado na lista de aceleração em X da bola para plotagem posterior
    lista_AceleracaoX_robo.append(aceleracaoXrobo)
    # mesma coisa para aceleração em Y
    aceleracaoYrobo = round(((float(lista_VelocidadeY_robo[i]) - float(lista_VelocidadeY_robo[i - 1])) / 0.02), 3)
    lista_AceleracaoY_robo.append(aceleracaoYrobo)
    print("Aceleração X do Robô:", aceleracaoXrobo)
    print("Aceleração Y do Robô:", aceleracaoYrobo)
    print()

# chama a função
aceleracaoRobo(lista_VelocidadeX_robo, lista_VelocidadeY_robo, listaT)
