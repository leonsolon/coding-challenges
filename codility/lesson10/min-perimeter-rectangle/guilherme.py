from math import floor
def solution(N): # O(sqrt(N)) - 100% em Correctness - 100% em Performance

    sqr_N = floor(N**(1/2))

    factor = 1
    for i in range(sqr_N, 0, -1):
        if N % i == 0:
            factor = i
            break

    min_perimeter = 2 * (factor + N/factor)


    return int(min_perimeter)

print(solution(982451653))