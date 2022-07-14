# 60% de resultado
# 100% correctness
# 20% performance
from itertools import accumulate
def solution(A):
    somas = []
    min_avg = 10000
    for i in range(0, len(A)):
        lista = A[i:]
        somas.append(list(accumulate(lista))) # salvando as somas das possibilidades de slice
    for i in range(len(somas)):
        for j in range(1, len(somas[i])):
            avg = somas[i][j]/(j+1) # calculando a média, excluindo as somas que contém um único elemento - índice j == 0
            if avg < min_avg:
                min_avg = avg
                position = i
    return position
