# Correctnes 87% performance 100% - 91% overall

from collections import Counter


def solution(A):
    # write your code in Python 3.6

    if len(A) == 0:
        return -1
    elif len(A) == 1:
        return 0
    elif len(A) == 2:
        if A[0] == A[1]:
            return [0, 1]
        else:
            return -1
    else:
        set_A = set(A)

        if len(set_A) == 1:
            return list(range(len(A)))

    dominant_counter = Counter(A)

    sorted_counts = sorted(dominant_counter.values())

    if sorted_counts[-1] == sorted_counts[-2]:
        return -1
    elif sorted_counts[-1] > len(A) // 2:
        dominant = dominant_counter.most_common(1)[0][0]

        print(dominant)

        return A.index(dominant)

    return -1


assert solution([2147483647]) == 0

