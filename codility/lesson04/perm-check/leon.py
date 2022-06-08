# O(N) or O(N * log(N)), 100%
def solution(A):
    # write your code in Python 3.6

    perm_set = set(range(1, len(A)+1))

    for element in A:
        if element in perm_set:
            perm_set.remove(element)
        else:
            return 0

    if len(perm_set) > 0:
        return 0
    else:
        return 1
