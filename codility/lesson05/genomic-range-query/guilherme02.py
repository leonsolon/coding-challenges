def solution1(S, P, Q): # O(N**2) - 100% em Correctness - 0% em Performance
    retorno = []
    for i,p in enumerate(P):
        usefull_S = S[p:Q[i]+1]
        min_usefull_S= min(usefull_S)

        if min_usefull_S == 'A':
            retorno.append(1)
        elif min_usefull_S == 'C':
            retorno.append(2)
        elif min_usefull_S == 'G':
            retorno.append(3)
        elif min_usefull_S == 'T':
            retorno.append(4)
    return retorno