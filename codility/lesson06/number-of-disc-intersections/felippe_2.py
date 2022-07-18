# Lesson 6 Ex 04
# NumberOfDiscIntersections
# 100%
import bisect
def solution(A):
    maximo = []
    minimo = []
    count = 0
    for i, e in enumerate(A): # salvando os limites de cada disco
        maximo.append(i+e)
        minimo.append(i-e)
    max_sorted = sorted(maximo)
    min_sorted = sorted(minimo)
    for i in range(len(A)):
        intersection = bisect.bisect(min_sorted, maximo[i]) 
        count += intersection - 1 - i # retirar i para não contar as intersecções repetidas
        if count > 10_000_000:
            return -1
    return count
