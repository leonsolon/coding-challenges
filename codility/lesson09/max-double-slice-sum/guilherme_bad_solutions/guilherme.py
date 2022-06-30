def get_max_sum(A=[]):
    max_sums = []
    current_sum = 0

    for a in A:
        if a > a + current_sum:
            current_sum = max(a,0)
        else:
            current_sum += a

        if current_sum <0:
            current_sum = 0

        max_sums.append(current_sum)

    return  max_sums

def solution(A=[]): # O(N) - 100% em Correctness - 85% em Performance
    A = A[1:-1]
    A_reverse = A[::-1]

    len_A = len(A)
    max_A = max(A)
    min_A = min(A)
    sum_A = sum(A)

    if len_A <=1:
        return 0
    elif len_A == 2:
        return max(max_A, 0)

    if min_A >0:
        return sum_A - min_A



    max_sum_A = get_max_sum(A)
    print(max_sum_A)


    max_sum_A_reverse = get_max_sum(A_reverse)
    max_sum_A_reverse = max_sum_A_reverse[::-1]
    print(max_sum_A_reverse)
    max_sum_A_reverse = max_sum_A_reverse[2:] +[0]*2

    # print(max_sum_A, max_sum_A_reverse)

    max_sum_double_slice = 0
    for (slice1, slice2) in zip (max_sum_A, max_sum_A_reverse):
        max_sum_double_slice = max(max_sum_double_slice, slice1+ slice2)

    return max_sum_double_slice


print(solution([5, 1, 0, 0, 5])) # = 1
print(solution([5, 0, 1, 0, 5])) # = 1
print(solution([5, 0, 0, 1, 5])) # = 1
print(solution([5, 3, 2, -1, 5])) # = 1
# print(solution([1,3,4,2,-3,4,-10,1,1,4,-2,4,1])) # = 18
# print(solution([-2, -3, -4, 1, -5, -6, -7])) # = 1
# print(solution([5, 5, 5])) # = 0
# print(solution([-8, 10, 20, -5, -7, -4])) # = 30
# print(solution([5, 17, 0, 3])) # = 17
# print(solution([-10,-10,8,-1,3,-20,7,-1,4,-10,-10])) # = 20
# print(solution([3,2,6,-1,4,5,-1,2])) # = 17
# print(solution([3,2,6,-1,4,5,1,2])) # = 18
# print(solution( [ 2, 3, 5,-10]*3)) # = 20
# print(solution( [1, 2, 3, 4,5,-15]*50)) # = 30
# print(solution( [ 2, 3,-3,-2, 4,5,-15]*4)) # = 18
# print(solution( [6, 1, 5, 6, 4, 2, 9, 4])) # = 26
# print(solution( [0, 10, -5, -2, 0])) # = 10
# print(solution( [-8, 10, 20, -5, -7, -4])) # = 30