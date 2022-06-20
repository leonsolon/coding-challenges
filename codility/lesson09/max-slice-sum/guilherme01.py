def solution (A):
    max_ending = -float('inf')
    max_slice = -float('inf')
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)

    return max_slice

print(solution([3, 2, -6, 4, 0]))
print(solution([-10]))
print(solution([20,-10,15,-2,-3,-1]))
print(solution([-2,1]))
print(solution([1,-2]))
print(solution([-2, 1, 3]))
