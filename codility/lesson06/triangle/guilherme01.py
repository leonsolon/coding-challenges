def solution(A):
    # write your code in Python 3.6
    A.sort()

    for i, a in enumerate(A):
        if i+2 < len(A) and a >=0:
            if a + A[i+1] > A[i+2]:
                return 1

    return 0