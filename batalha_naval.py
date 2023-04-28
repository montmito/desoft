def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    elif orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota

def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(frota):
    
    grid = [[0 for i in range(10)] for j in range(10)]
    
   
    for nome_navio, posicoes_navio in frota.items():
        for posicoes in posicoes_navio:
            for posicao in posicoes:
                linha, coluna = posicao
                grid[linha][coluna] = 1
    
    return grid


def afundados(frota, tabuleiro):
    navios_afundados = 0
    for nome_navio, posicoes_navio in frota.items():
        for posicao_navio in posicoes_navio:
            afundou = True
            for coordenadas in posicao_navio:
                if tabuleiro[coordenadas[0]][coordenadas[1]] != 'X':
                    afundou = False
                    break
            if afundou:
                navios_afundados+=1

    return navios_afundados