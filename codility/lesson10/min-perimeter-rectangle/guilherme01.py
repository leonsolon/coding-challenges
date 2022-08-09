# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def get_factors(N):
    i=1
    sqrt_N = N**(1/2)
    factors = set()
    while i <= sqrt_N:
        if N % i ==0:
            factors.add(i)
            factors.add(int(N/i))
        i += 1
    return factors


def solution(N): # O(sqrt(N)) - 100% em Correctness - 100% em Performance
    factors = list(get_factors(N))
    factors.sort()
    len_factors = len(factors)
    side = factors[len_factors//2]
    perimeter = 2*(side + N/side)
    return int(perimeter)