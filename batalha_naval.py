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


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        linha, coluna = posicao
        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            return False
        for navio in frota.values():
            for posicoes_navio in navio:
                if posicao in posicoes_navio:
                    return False
    return True


frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}


embarcacoes = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1,
}

qt_embarcacoes = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4,
}

for nome, quantidade in qt_embarcacoes.items():
    for i in range(quantidade):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {embarcacoes[nome]}")
        while True:
            linha = int(input("Linha:"))
            coluna = int(input("Coluna:"))
            if nome == "submarino":
                if posicao_valida(frota, linha, coluna, "vertical", embarcacoes[nome]):
                    frota[nome].append([[linha, coluna]])
                    break
                else:
                    print("Esta posição não está válida!")
                    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {embarcacoes[nome]}")
            else:
                orientacao = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
                if posicao_valida(frota, linha, coluna, orientacao, embarcacoes[nome]):
                    frota = preenche_frota(frota, nome, linha, coluna, orientacao, embarcacoes[nome]) 
                    break
                else:
                    print("Esta posição não está válida!")
                    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {embarcacoes[nome]}")
print (frota)