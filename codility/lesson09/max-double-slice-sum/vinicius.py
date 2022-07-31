'''
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''

def solution(A):
    if len(A) == 3:
        return 0
    round_one_sum = 0
    round_two_sum = 0
    end_sum_round_one = -float('inf')
    end_sum_round_two = -float('inf')
    end_index_round_one = 0
    menor_num = min(A[1:-1])
    for index, num in enumerate(A[1:-1]):
        if num == menor_num:
            end_index_round_one = index
            break
        if num >= end_sum_round_one + num:
            end_sum_round_one = num
        else:
            end_sum_round_one = end_sum_round_one + num
        if round_one_sum < end_sum_round_one:
            round_one_sum = end_sum_round_one
            end_index_round_one = index
    if end_index_round_one+1 == len(A):
        return round_one_sum
    else:
        for i in range(end_index_round_one+2,len(A)-1):
            end_sum_round_two = max(end_sum_round_two+A[i],A[i])
            round_two_sum = max(end_sum_round_two, round_two_sum)
    return round_one_sum + round_two_sum

'''
CORRECTNESS 100%
PERFORMANCE 28%
TOTAL       61%
'''

def solution(A):
    if len(A) == 3:
        return 0
    round_one_sum = 0
    round_two_sum = 0
    end_sum_round_one = -float('inf')
    end_sum_round_two = -float('inf')
    menor_num_index = A[1:-1].index(min(A[1:-1]))
    print(menor_num_index)
    for num in A[1:menor_num_index+1]:
        if num >= end_sum_round_one + num:
            end_sum_round_one = num
        else:
            end_sum_round_one = end_sum_round_one + num
        if round_one_sum < end_sum_round_one:
            round_one_sum = end_sum_round_one
    print(round_one_sum)
    for num2 in A[menor_num_index+2:-1]:
        end_sum_round_two = max(end_sum_round_two+num2, num2)
        round_two_sum = max(end_sum_round_two, round_two_sum)
    print(round_two_sum)
    return round_one_sum + round_two_sum

'''
CORRECTNESS 100%
PERFORMANCE 28%
TOTAL       61%
'''

def solution(A):
    if len(A) == 3:
        return 0
    round_one_sum = [0]*len(A)
    round_two_sum = [0]*len(A)
    for i in range(1, len(A)-2):
        round_one_sum[i] = max(round_one_sum[i-1] + A[i], 0)
    for i in range(len(A)-2, 1, -1):
        round_two_sum[i] = max(round_two_sum[i+1] + A[i], 0)
    max_slice_sum = round_one_sum[0] + round_two_sum[2]
    for i in range(1, len(A)-1):
        max_slice_sum = max(max_slice_sum, round_one_sum[i-1] + round_two_sum[i+1])
    return max_slice_sum

'''
TOTAL 100%
'''