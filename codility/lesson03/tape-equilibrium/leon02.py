# O(N)  100% Correctness 100% Performance

import math

def solution(A):
    # write your code in Python 3.6

    if len(A) == 2:
        return abs(A[0] - A[1])

    sum_left = A[0]
    sum_right = sum(A[1:])
    min_difference = abs(sum_left - sum_right)

    #print(f'first diff {min_difference}')

    for i in range(1, len(A)-1):
        sum_left += A[i]
        sum_right -= A[i]

        local_difference = abs(sum_left - sum_right)

        #print(f'{A[i]}, {sum_left}, {sum_right}, {local_difference}')

        if local_difference < min_difference:
            min_difference = local_difference

    return min_difference
