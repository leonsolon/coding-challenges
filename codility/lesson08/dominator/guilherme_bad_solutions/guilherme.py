def solution(A=[]): # O(N*log(N)) or O(N) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    len_A = len(A)
    set_A = set(A)
    len_set_A = len(set_A)

    if len_A==0:
        return -1

    A_sorted = sorted(zip(A, range(0,len_A)))

    if A.count(A_sorted[len_A//2][0]) > len_A/2:
        return A_sorted[len_A//2][1]

    return -1


print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
print(solution([2,2,2,2,3,3,4,4]))
print(solution([1, 2, 1,2]))