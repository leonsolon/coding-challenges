# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A=[]):
    len_A = len(A)
    if len_A == 0:
        return -1
    A_sorted = sorted(A)

    idx = len_A // 2
    dominator = A_sorted[idx]
    count = A.count(dominator)
    if count > len_A / 2:
        return A.index(dominator)
    return -1