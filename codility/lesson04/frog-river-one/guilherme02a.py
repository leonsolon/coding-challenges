import math

def solucao_existe(posicoes_necessarias, set_lista):
    for posicao in posicoes_necessarias:
        if posicao not in set_lista:
            return False
    return True

def obtem_posicoes_pendentes(posicoes_necessarias, set_lista):
    # print(f'posicoes_necessarias: {posicoes_necessarias} -set_lista: {set_lista}')
    posicoes_pendentes = posicoes_necessarias
    for posicao in set_lista:
        if posicao in posicoes_pendentes:
            posicoes_pendentes.remove(posicao)
            # print(f'posicao: {posicao} - posicoes_pendentes: {posicoes_pendentes}')
    return posicoes_pendentes

def solution1(X, A): # O(N) - 100% em Correctness - 60% em Performance
    # write your code in Python 3.6
    posicoes_necessarias = list(range(1, X + 1))

    if not(solucao_existe(posicoes_necessarias,set(A))):
        return -1

    lista = A
    posicao_minima = 0
    while True:
        sub_listas = []
        len_lista = len(lista)
        print(lista)
        if len_lista<=len(posicoes_necessarias):
            return posicao_minima + len_lista - 1
        sub_listas.append(lista[0:math.floor(len_lista/2)])
        sub_listas.append(lista[math.floor(len_lista / 2):])


        for i, sub_lista in enumerate(sub_listas):
            set_sub_lista = set(sub_lista)
            print(f'posicao_minima: {posicao_minima} - posicoes_necessarias {posicoes_necessarias} - sub_lista {sub_lista}')
            if solucao_existe(posicoes_necessarias, set_sub_lista):
                print(f'solução existe')
                lista = sub_lista
                break
            else:
                print(f'solução NÃO existe')
                posicao_minima += len(sub_lista)
                posicoes_necessarias = obtem_posicoes_pendentes(posicoes_necessarias,set(sub_lista))