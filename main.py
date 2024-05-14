import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def carrega_dados_bola(arquivo):
    dados_bola = []

    with open(arquivo, 'r') as base_dados:
        for linha in base_dados:
            instant_t, x_bola, y_bola, vx_bola, vy_bola, ax_bola, ay_bola = linha.strip().split(";")
            bola = {
                "t": float(instant_t),
                "x_bola": float(x_bola),
                "y_bola": float(y_bola),
                "vx_bola": float(vx_bola),
                "vy_bola": float(vy_bola),
                "ax_bola": float(ax_bola),
                "ay_bola": float(ay_bola)
            }
            dados_bola.append(bola)

    return dados_bola

def carrega_dados_robo(arquivo):
    dados_robo = []

    with open(arquivo, 'r') as base_dados:
        for linha in base_dados:
            instant_t, x_robo, y_robo, vx_robo, vy_robo, ax_robo, ay_robo = linha.strip().split(";")
            robo = {
                "t": float(instant_t),
                "x_robo": float(x_robo),
                "y_robo": float(y_robo),
                "vx_robo": float(vx_robo),
                "vy_robo": float(vy_robo),
                "ax_robo": float(ax_robo),
                "ay_robo": float(ay_robo)
            }
            dados_robo.append(robo)

    return dados_robo

def ponto_menor_distancia(dados_bola, x_robo, y_robo):
    dados_bola_menor_dist = {}
    menor_distancia = 100
    indice_menor_dis = -1

    for registro in dados_bola:
        distancia = math.sqrt((registro['x_bola'] - x_robo)**2 + (registro['y_bola'] - y_robo)**2)

        if distancia < menor_distancia:
            menor_distancia = distancia
            indice_menor_dis = dados_bola.index(registro)


    dados_bola_menor_dist = dados_bola[indice_menor_dis]

    return dados_bola_menor_dist

def calcula_velocidade_interceptacao(posicao_bola, posicao_robo, instante):
    velocidade = (posicao_bola - posicao_robo) / instante

    return velocidade

def calcula_aceleracao_interceptacao(velocidade, instante):
    velocidade_inicial = 0
    aceleracao = (velocidade - velocidade_inicial) / instante

    return aceleracao

def trajetoria_robo(ponto_intercep, x_inicial, y_inicial, trajetoria_bola):
    vx_inicial = 0
    vy_inicial = 0
    vx_intercep = calcula_velocidade_interceptacao(ponto_intercep['x_bola'], x_inicial, ponto_intercep['t'])
    vy_intercep = calcula_velocidade_interceptacao(ponto_intercep['y_bola'], y_inicial, ponto_intercep['t'])

    aceleracao_x = calcula_aceleracao_interceptacao(vx_intercep, ponto_intercep['t'])
    aceleracao_y = calcula_aceleracao_interceptacao(vy_intercep, ponto_intercep['t'])

    dados_trajetoria_robo = []

    for instante in range(len(trajetoria_bola)):
        if trajetoria_bola[instante]['t'] <= ponto_intercep['t']:
            vx_robo = vx_inicial + (aceleracao_x * trajetoria_bola[instante]['t'])
            vy_robo = vy_inicial + (aceleracao_y * trajetoria_bola[instante]['t'])

            x_robo = x_inicial + (vx_robo * trajetoria_bola[instante]['t'])
            y_robo = y_inicial + (vy_robo * trajetoria_bola[instante]['t'])

            distancia = math.sqrt((ponto_intercep['x_bola'] - x_robo)**2 + (ponto_intercep['y_bola'] - y_robo)**2)

            robo = {
                "t": trajetoria_bola[instante]['t'],
                "x_robo": x_robo,
                "y_robo": y_robo,
                "vx_robo": vx_robo,
                "vy_robo": vy_robo,
                "ax_robo": aceleracao_x,
                "ay_robo": aceleracao_y,
                "distancia": distancia
            }

            dados_trajetoria_robo.append(robo)

    return dados_trajetoria_robo

def salva_dados_robo(dados_trajetoria):
    with open('dados_trajetoria_robo.txt', 'w') as arquivo:
        for linha in dados_trajetoria:
            arquivo.write(f"{linha['t']};{linha['x_robo']};{linha['y_robo']};{linha['vx_robo']};{linha['vy_robo']};{linha['ax_robo']};{linha['ay_robo']};{linha['distancia']}\n")


def exibe_simulacao(dados_bola, dados_robo):
    x_plot_b = []
    y_plot_b = []
    x_plot_r = []
    y_plot_r = []

    for linha in range(len(dados_robo)):
        xb = dados_bola[linha]['x_bola']
        yb = dados_bola[linha]['y_bola']
        xr = dados_robo[linha]['x_robo']
        yr = dados_robo[linha]['y_robo']

        x_plot_b.append(xb)
        y_plot_b.append(yb)
        x_plot_r.append(xr)
        y_plot_r.append(yr)

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.set_xlim(0, 10)
    ax2.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax2.set_ylim(0, 8)

    img = plt.imread("campo.jpg")
    ax1.imshow(img, zorder=0, extent=[0, 10, 0, 8])

    def update_data(frame):
        ax1.plot(x_plot_b[:frame], y_plot_b[:frame], color='white', ms=2, ds='steps', marker='.')
        ax2.plot(x_plot_r[:frame], y_plot_r[:frame], color='black', ms=2, ds='steps', marker='.')

        ax1.legend(['Trajetória bola','Trajetória robô'], labelcolor=['white', 'black'], loc=1)

        fig.suptitle('Simulação interceptação', fontsize=16)

        return ax1, ax2

    animation = FuncAnimation(fig=fig, func=update_data, frames=len(x_plot_r), repeat=False, interval=1)

    plt.show()

def plota_graficos_posicao(dados_bola, dados_robo):
    tempo = []
    x_robo = []
    y_robo = []

    x_bola = []
    y_bola = []

    for linha in range(len(dados_robo)):
        tempo.append(dados_bola[linha]['t'])
        x_bola.append(dados_bola[linha]['x_bola'])
        y_bola.append(dados_bola[linha]['y_bola'])

        x_robo.append(dados_robo[linha]['x_robo'])
        y_robo.append(dados_robo[linha]['y_robo'])

    fig, eixo = plt.subplots(1, 2, sharey=True)

    eixo[0].set_xlabel("tempo (s)")
    eixo[1].set_xlabel("tempo (s)")
    eixo[0].set_ylabel("posicao X (m)")
    eixo[1].set_ylabel("posicao Y (m)")

    plot_x_bola, = eixo[0].plot(tempo, x_bola)
    plot_x_robo, = eixo[0].plot(tempo, x_robo)
    plot_y_bola, = eixo[1].plot(tempo, y_bola)
    plot_y_robo, = eixo[1].plot(tempo, y_robo)

    fig.legend((plot_x_bola, plot_x_robo), ('bola', 'robo'), loc='upper right')

    fig.suptitle('Posição em função do tempo', fontsize=16)

    plt.savefig("graficos/grafico_posicao.pdf")
    plt.close()

def plota_graficos_velocidade(dados_bola, dados_robo):
    tempo = []
    vx_robo = []
    vy_robo = []

    vx_bola = []
    vy_bola = []

    for linha in range(len(dados_robo)):
        tempo.append(dados_bola[linha]['t'])
        vx_bola.append(dados_bola[linha]['vx_bola'])
        vy_bola.append(dados_bola[linha]['vy_bola'])

        vx_robo.append(dados_robo[linha]['vx_robo'])
        vy_robo.append(dados_robo[linha]['vy_robo'])

    fig, eixo = plt.subplots(1, 2, sharey=True)

    eixo[0].set_xlabel("tempo (s)")
    eixo[1].set_xlabel("tempo (s)")
    eixo[0].set_ylabel("velocidade X (m/s)")
    eixo[1].set_ylabel("velocidade Y (m/s)")

    plot_vx_bola, = eixo[0].plot(tempo, vx_bola)
    plot_vx_robo, = eixo[0].plot(tempo, vx_robo)
    plot_vy_bola, = eixo[1].plot(tempo, vy_bola)
    plot_vy_robo, = eixo[1].plot(tempo, vy_robo)

    fig.legend((plot_vx_bola, plot_vx_robo), ('bola', 'robo'), loc='upper right')

    fig.suptitle('Velocidade em função do tempo', fontsize=16)

    plt.savefig("graficos/grafico_velocidade.pdf")
    plt.close()

def plota_grafico_dist_relativa(dados_robo):
    tempo = []
    distancia = []
    
    for linha in range(len(dados_robo)):
        tempo.append(dados_robo[linha]['t'])
        distancia.append(dados_robo[linha]['distancia'])

    fig, eixo = plt.subplots()

    eixo.plot(tempo, distancia)
    eixo.set_xlabel("tempo (s)")
    eixo.set_ylabel("distancia (m)")

    fig.suptitle('Distância relativa em função do tempo', fontsize=16)

    plt.savefig("graficos/grafico_dist_relativa.pdf")

    plt.close()

def main():
    path_arq = 'dados_trajetoria_bola.txt'
    dados_bola = carrega_dados_bola(path_arq)

    while True:
        x_robo = float(input("\nDigite a posição X do robô: "))
        y_robo = float(input("Digite a posição Y do robô: "))

        ponto_interceptacao = ponto_menor_distancia(dados_bola, x_robo, y_robo)

        dados_interceptacao = trajetoria_robo(ponto_interceptacao, x_robo, y_robo, dados_bola)

        salva_dados_robo(dados_interceptacao)

        exibe_simulacao(dados_bola, dados_interceptacao)

        plota_graficos_posicao(dados_bola, dados_interceptacao)
        plota_graficos_velocidade(dados_bola, dados_interceptacao)
        plota_grafico_dist_relativa(dados_interceptacao)

        input_usuario = input("\nGostaria de simular novamente? (S/N) ")

        if input_usuario in ['S', 's']:
            True
        else:
            break

main()
