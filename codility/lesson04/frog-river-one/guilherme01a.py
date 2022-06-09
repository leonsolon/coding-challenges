def solution(X, A): # O**2 - 100% em Correctness - 20% em Performance
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
