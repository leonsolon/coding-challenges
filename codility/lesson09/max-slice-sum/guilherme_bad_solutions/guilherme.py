def solution(A):
    # write your code in Python 3.6
    max_sum = -float('inf')
    current_sum = -float('inf')
    if min(A) >= 0:
        return sum(A)

    if max(A) <=0:
        return max(A)

    for i, a in enumerate(A):
        if current_sum > 0 and a > 0:
            current_sum += a
        elif a > current_sum:
            current_sum = a
        else:
            if max_sum < current_sum:
                max_sum = current_sum
            if current_sum + a >0:
                current_sum += a
            else:
                current_sum = -float('inf')

    else:
        if max_sum < current_sum:
            max_sum = current_sum

    return max_sum

print(solution([3, 2, -6, 4, 0]))
print(solution([-10]))
print(solution([20,-10,15,-2,-3,-1]))
print(solution([-2,1]))
print(solution([1,-2]))
print(solution([-2, 1, 3]))