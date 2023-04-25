def mais_lancamentos(series, ano):
    lancamentos_no_ano = dict()
    que_mais_lancaram = []
    max_lancamentos = 0
    for serie in series:
        plataforma = serie['plataforma']
        titulo = serie['titulo']
        ano_estreia = serie['ano_estreia']
        if ano == ano_estreia:
            if plataforma not in lancamentos_no_ano.keys():
                lancamentos_no_ano[plataforma] = 1
            else:
                lancamentos_no_ano[plataforma] +=1

    for plataforma, n_lancamentos in lancamentos_no_ano.items():
        if n_lancamentos > max_lancamentos:
            max_lancamentos = n_lancamentos
            que_mais_lancaram = [plataforma]
        elif n_lancamentos == max_lancamentos:
            que_mais_lancaram.append(plataforma)

    return que_mais_lancaram