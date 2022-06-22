'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
'''

def solution(A):
    N = len(A)
    A = sorted(A)
    if A[0] != 1:
        return 0
    if len(set(A)) != N:
        return 0
    B = [i for i in range(1,N+1)]
    formula_pa_A = ((((A[0]+A[-1])*N)/2))
    formula_pa_B = ((((B[0]+B[-1])*N)/2))
    if formula_pa_A == formula_pa_B:
        return 1
    else:
        return 0
