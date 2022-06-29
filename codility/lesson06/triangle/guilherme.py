# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A=[]):
    A.sort()
    i = 0
    while i < len(A) and A[i] <= 0:
        i += 1

    if i < len(A):
        A = A[i:]
    else:
        return 0

    len_A = len(A)
    if len_A < 3:
        return 0

    for i, a in enumerate(A):
        if i + 2 < len_A and a + A[i + 1] > A[i + 2]:
            return 1

    return 0