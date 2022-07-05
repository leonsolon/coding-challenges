def solution(A):
    # write your code in Python 3.6
    len_A = len(A)

    if len_A < 2:
        return 0

    min_A = min(A)
    max_A = max(A)
    profit = 0
    max_profit = 0
    actual_min = float('inf')

    for a in A:
        if a < actual_min:
            actual_min = a

        profit = a - actual_min
        if profit > max_profit:
            max_profit = profit
            if max_profit == max_A - min_A:
                return int(max_profit)
    return max_profit

print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
