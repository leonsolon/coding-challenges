def solution(S, P, Q): # O(N**2) - 100% em Correctness - 100% em Performance
    retorno = []
    for i,p in enumerate(P):
        usefull_S = S[p:Q[i]+1]

        if 'A' in usefull_S:
            retorno.append(1)
        elif 'C' in usefull_S:
            retorno.append(2)
        elif 'G' in usefull_S:
            retorno.append(3)
        else:
            retorno.append(4)
    return retorno
