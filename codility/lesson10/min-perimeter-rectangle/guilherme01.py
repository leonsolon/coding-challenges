# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def get_factors(N):
    i=1
    factors = set()
    while i*i <= N:
        if N % i ==0:
            factors.add(i)
            factors.add(N/i)
        i+=1
    return factors


def solution(N): # O(sqrt(N)) - 100% em Correctness - 100% em Performance
    factors = list(get_factors(N))
    factors.sort()
    len_factors = len(factors)
    side = factors[len_factors//2]
    perimeter = 2*(side + N/side)
    return int(perimeter)