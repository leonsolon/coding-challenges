# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(A):
    A.sort()
    if len(A) <= 5:
        B = A
    else:
        B = A[:2] + A[-3:]

    comb_B = combinations(B,3)
    max_product = -float('inf')
    for itens in comb_B:
        product = itens[0]*itens[1]*itens[2]
        max_product = max(product,max_product)

    return max_product