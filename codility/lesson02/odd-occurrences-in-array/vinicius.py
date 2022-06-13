def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    for n in range(0, len(A),2):
        if A[n] == A[n+1] and n+3 != len(A):
            continue
        elif A[n] == A[n+1] and n+3 == len(A):
            return A[-1]
        else:
            return A[n]
