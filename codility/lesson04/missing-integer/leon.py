# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from bisect import bisect_left

def solution(A):
    A = set(A)
    A = sorted(A)

    bisected = bisect_left(A, 1)

    A = A[bisected:]

    if len(A) == 0:
        return 1

    if A[0] != 1:
        return 1

    previous = 1

    for index in range(1,len(A)):
        if A[index] != previous + 1:
            return previous + 1
        else:
            previous += 1

    return A[-1] + 1


