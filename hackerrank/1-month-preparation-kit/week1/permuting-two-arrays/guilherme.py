def twoArrays(k, A=[], B=[]):
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        if a + b < k:
            return 'NO'
    return 'YES'