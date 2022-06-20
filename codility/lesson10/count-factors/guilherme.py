def solution(N): # O(sqrt(N)) - 100% em Correctness - 100% em Performance
    sqr_N = N**(1/2)
    factors = 0
    i = 1
    while i <= sqr_N:
        if N % i == 0:
            factors +=2
        if i == sqr_N:
            factors -=1
        i+=1
    return factors
print(solution(36))