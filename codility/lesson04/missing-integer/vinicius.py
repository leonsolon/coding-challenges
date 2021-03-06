'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):
    set_A = set(A)
    max_set_A = max(set_A) if max(set_A) >= 0 else 1
    aux = list(range(1,max_set_A+1))
    if set(aux).issubset(set_A):
        return max_set_A + 1
    for i in aux:
        if i not in set_A:
            return i
    return max_set_A + 1
