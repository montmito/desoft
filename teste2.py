def pet_pode_viajar(info_pet, limites, passagens):
    peso_total = info_pet[2] + info_pet[3]
    if peso_total > limites[1]:
        return False

    caixa = info_pet[4]
    if caixa[0] > limites[2][0] or caixa[1]>limites[2][1] or caixa[2]>limites[2][2]:
        return False

    if info_pet[5] == 'N':
        return False

    quantidade_pets_vendidos = 0
    for passagem in passagens:
        if 'pet_cabine' in passagem[1]:
            quantidade_pets_vendidos += 1
    if quantidade_pets_vendidos >= limites[0]:
        return False

    return True