# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    curent_sum = 0
    max_sum = -float('inf')
    for i, a in enumerate(A):
        curent_sum = max(a, curent_sum + a)
        max_sum = max(curent_sum, max_sum)

    return max_sum