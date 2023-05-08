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