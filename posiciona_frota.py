def posiciona_frota(frota):
    
    grid = [[0 for i in range(10)] for j in range(10)]
    
   
    for nome_navio, posicoes_navio in frota.items():
        for posicoes in posicoes_navio:
            for posicao in posicoes:
                linha, coluna = posicao
                grid[linha][coluna] = 1
    
    return grid