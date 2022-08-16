def solution(N): # O(N) - 100% em Correctness - 50% em Performance
    # write your code in Python 3.6
    # Numerdo de divisores é multiplicação de 1+  potências de seus fatores primos
    # de 24 = 2^3*3^1 - Divisores de 24 = (3+1)*(1+1) = 8
    prime_factors = 1

    i=2
    add = 1
    while i <= N:
        count = 0
        prime = False
        while N % i ==0:
            count += 1
            N = N/i

        if count>0 :
            prime_factors *= (count+1)
        if i==3:
            add = 2
        i+= add



    return prime_factors

print(solution(780291637))