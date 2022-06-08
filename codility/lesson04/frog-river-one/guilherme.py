import random
def gera_lista(tamanho, min, max):
    lista = []
    for i in range(0, tamanho):
        lista.append(random.randint(min,max))
    print(lista)
    return lista

def gera_lista_sequencial(tamanho):
    return list(range(1, tamanho+1))


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

def solution(X, A): # O(N) - 100% em Correctness - 60% em Performance
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


def solution4(X, A): # O**2 - 100% em Correctness - 20% em Performance
    # write your code in Python 3.6
    posicoes_necessarias = list(range(1, X+1))


    for K, elemento_A in enumerate(A):
        if elemento_A in posicoes_necessarias:
            posicoes_necessarias.remove(elemento_A)
            # print(f'{K} - {posicoes_necessarias}')
            if len(posicoes_necessarias)==0:
                return K
    return -1

def solution3(X, A): # O**2 - 100% em Correctness - 20% em Performance
    # write your code in Python 3.6
    posicoes_necessarias = list(range(1, X+1))
    # print(posicoes_necessarias)
    set_A = set(A)
    if len(set_A) == X:
        for K, elemento_A in enumerate(A):
            if elemento_A in posicoes_necessarias:
                posicoes_necessarias.remove(elemento_A)
                # print(f'{K} - {posicoes_necessarias}')
                if len(posicoes_necessarias)==0:
                    return K
    else:
        return -1

def solution2(X, A): # O**2 - 100% em Correctness - 0% em Performance
    # write your code in Python 3.6
    primeira_posicao = []
    for i in range(1, X+1):
        if i in A:
            primeira_posicao.append(A.index(i))
        else:
            return -1
    return max(primeira_posicao)

A = [2, 1, 2, 5, 4, 1, 5, 4, 4, 2, 4, 2, 1, 2, 4, 2, 4, 2, 5, 2, 5, 1, 4, 5, 5, 2, 2, 1, 4, 2, 2, 1, 5, 4, 2, 4, 5, 5, 1, 4, 4, 2, 4, 1, 5, 5, 2, 4, 3, 4, 1, 5, 3, 2, 1, 5, 4, 2, 4, 3, 4, 2, 5, 1, 5, 1, 1, 3, 2, 2, 3, 2, 2, 1, 2, 2, 5, 4, 4, 3, 3, 5, 4, 3, 3, 5, 5, 4, 3, 5, 3, 3, 3, 1, 3, 3, 4, 1, 1, 1, 3, 1, 5, 1, 2, 1, 2, 2, 5, 1, 5, 2, 5, 5, 4, 4, 2, 3, 5, 2, 3, 5, 5, 2, 5, 3, 4, 2, 2, 1, 4, 3, 5, 2, 4, 5, 5, 4, 3, 2, 5, 5, 5, 4, 1, 3, 5, 3, 1, 1, 4, 2, 1, 3, 3, 4, 4, 5, 2, 1, 4, 4, 5, 3, 5, 1, 3, 4, 3, 1, 2, 5, 2, 2, 3, 3, 1, 1, 3, 3, 5, 5, 2, 1, 1, 4, 1, 2, 3, 4, 5, 5, 2, 3, 5, 5, 1, 5, 1, 2]
# A = [1, 3, 1, 4, 2, 3, 5, 4]
A = gera_lista_sequencial(30000)
X = max(A)
a = solution(X, A)
print(a)
