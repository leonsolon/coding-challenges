# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A)==0:
        return 0
    min_value = float('inf')
    max_profit = 0
    max_max_profit = max(A) - min(A)
    for i, a in enumerate(A):
        min_value = min(min_value,a)
        profit = a - min_value
        max_profit = max(max_profit,profit)
        if max_profit >= max_max_profit:
            return max_profit

    return max_profit