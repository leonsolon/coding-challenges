def pageCount(n, p):
    folhas = n//2
    folha_desejada = p//2
    return min(folha_desejada, folhas - folha_desejada)