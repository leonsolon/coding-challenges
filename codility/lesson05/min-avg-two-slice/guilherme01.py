def solution(A): # O(N ** 3) - 100% em Correctness - 0% em Performance

    # write your code in Python 3.6
    minimal_avg = sum(A) / (len(A) + 1)
    initial_p = 0
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            avg = sum(A[i:j + 1]) / (j - i + 1)
            if avg >= minimal_avg:
                pass
            else:
                minimal_avg = avg
                initial_p = i

    return initial_p

print(solution([-3, -5, -8, -4, -10]))
print(solution([4, 2, 2, 5, 1,5,8]))