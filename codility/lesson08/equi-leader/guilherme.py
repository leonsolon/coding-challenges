# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter


def solution(A=[]):
    # write your code in Python 3.6
    count_A = Counter(A)
    count_A_right = count_A.copy()
    count_A_left = {}
    count_A_left['outros'] = 0
    len_A = len(A)
    equileader = 0
    for i, a in enumerate(A):
        if i== len_A-1:
            break
        len_left = i + 1
        if count_A[a] < len_A/2:
            if a in count_A_left:
                count_A_left['outros'] += count_A_left.pop(a) + 1
            else:
                count_A_left['outros'] += 1
        else:
            if a in count_A_left:
                count_A_left[a] += 1
            else:
                count_A_left[a] = 1



        if a in count_A_right:
            if count_A_right[a] == 1:
                count_A_right.pop(a)
            else:
                count_A_right[a] -= 1
        len_right = len_A - len_left


        (leader_left, count_leader_left) = max(count_A_left.items(),key=lambda x:x[1])

        if count_leader_left > len_left/2 and count_A_right[leader_left] > len_right/2:
            equileader +=1

    return equileader

assert solution([4, 3, 4, 4, 4, 2]) == 2
assert solution([]) == 0
assert solution([4]*1000000) == 1000000-1