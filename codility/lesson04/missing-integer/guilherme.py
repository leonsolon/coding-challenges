def solution(A):
    # write your code in Python 3.6
    set_A = set(A)
    for i in range(1, len(set_A)+2):
        if i not in set_A:
            return i