# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from math import ceil, floor

def solution(A, B, K):
    first = ceil(A/K)
    last = floor(B//K)
    return last-first+1