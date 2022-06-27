def solution(A): # O(N) or O(N ** 2) - 100% em Correctness - 60% em Performance

    # write your code in Python 3.6
    minimal_avg = sum(A) / (len(A))
    initial_p = 0
    for i in range(0, len(A)-1):
        for j in range(i + 1, len(A)):
            j_1 = j + 1
            avg = sum(A[i:j_1]) / (j_1 - i)
            if avg < minimal_avg:
                minimal_avg = avg
                initial_p = i
            if j_1 < len(A)-1 and avg < A[j_1]:
                break
    return initial_p

print(solution([-3, -5, -8, -4, -10]))
print(solution([4, 2, 2, 5, 1,5,8]))