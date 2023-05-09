import random
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

<<<<<<< HEAD
# Jogadas do jogador

# Jogadas do oponente
=======

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
#print (frota)
>>>>>>> 34ee08b61c62b8720441e9c91248a831f9771718

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

posicao_jo = []
posicao_op = []

while jogando:
    print (monta_tabuleiro(tabuleiro_jogador, tabuleior_oponente))
    linha = int(input("Informe a linha em que deseja atacar (0-9): "))
    if linha <= 9 and linha >= 0:
        break
        print("Linha inválida!")
        
    coluna = int(input("Informe a coluna em que deseja atacar (0-9): "))
    if coluna <= 9 and coluna >= 0:
        break
        print("Coluna inválida!")
    
    if (linha, coluna) in posicao_jo:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        continue
    posicao_jo.append((linha, coluna))
    
    faz_jogada(tabuleiro_oponente, linha, coluna)
    
    if afundados(frota_oponente, tabuleiro_oponente) == len(navios):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
        
        
    if afundados(frota_oponente, tabuleiro_oponente) != len(navios):
        
        while True:
            linha_op = random.randint(0, 9)
            coluna_op = random.randint(0, 9)

            if (linha_op, coluna_op) not in posicoes_oponente_informadas:
                break

        posicoes_oponente_informadas.append((linha_oponente, coluna_oponente))
        print(f"Seu oponente está atacando na linha {linha_op} e coluna {coluna_op}")

        faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        if afundados(frota, tabuleiro_jogador) == len(navios):
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
