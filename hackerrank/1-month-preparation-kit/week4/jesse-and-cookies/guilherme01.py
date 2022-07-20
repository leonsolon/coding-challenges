from bisect import insort # Não passou em 11/27 testes por performance
def cookies(k, A):
    if len(A)<=1:
        return -1
    A.sort()
    count = 0
    while min(A) <= k:
        least_sw = A.pop(0)
        second_least_sw = A.pop(0)
        new_sw = least_sw + 2*second_least_sw
        insort(A, new_sw)
        if len(A)<=1:
            return -1
        count += 1
    return count