def solution(X, A): # O**2 - 100% em Correctness - 0% em Performance
    # write your code in Python 3.6
    primeira_posicao = []
    for i in range(1, X+1):
        if i in A:
            primeira_posicao.append(A.index(i))
        else:
            return -1
    return max(primeira_posicao)