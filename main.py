#Declarando as listas que serão usadas
listaT = []
listaX = []
listaY = []
coordenadas = [] #Lista com o tempo, x e y de cada linha do txt

#Pede posição inicial do robô
posicaoXrobo = float(input("Digite a posição inicial do robô no eixo X: "))
posicaoYrobo = float(input("Digite a posição inicial do robô no eixo Y: "))

#Abre o arquivos e lê as linhas
with open("trajetoria.txt", "r+") as arquivo:
  #Para cada linha lida
  for linha in arquivo.readlines():
    linha = linha.replace(",", ".") #Substitui a vírgula por ponto
    coordenadas = linha.split() #Divide a linha em três partes
    listaT.append(coordenadas[0]) #Adiciona o tempo na lista 
    listaX.append(coordenadas[1]) #Adiciona o X na lista 
    listaY.append(coordenadas[2]) #Adiciona o Y na lista

#Print das listas para verificação
print(listaT)
print()
print(listaX)
print()
print(listaY)
