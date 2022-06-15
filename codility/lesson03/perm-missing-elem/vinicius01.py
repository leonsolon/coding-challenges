'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.

Write a function:
def solution(A)
that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

def solution(A):
    if len(A) == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    A.sort()
    B = [x+1 for x in range(0, len(A))]
    for i in range(0, len(A)):
        if A == B:
            return B[-1]+1
        if B[i] - A[i] == 0:
            continue
        else:
            return B[i]

"""
RESULTADO

SCORE: 50% CORRECTNESS: 80% PERFORMANCE: 20%

Analysis
Detected time complexity:
O(N ** 2)
expand allExample tests
▶example
example test✔OK
expand allCorrectness tests
▶empty_and_single
empty list and single element✘RUNTIME ERROR
tested program terminated with exit code 1
▶missing_first_or_last
the first or the last element is missing✔OK
▶single
single element✔OK
▶double
two elements✔OK
▶simple
simple test✔OK
expand allPerformance tests
▶medium1
medium test, length = ~10,000✔OK
▶medium2
medium test, length = ~10,000✘TIMEOUT ERROR
running time: 1.600 sec., time limit: 0.192 sec.
▶large_range
range sequence, length = ~100,000✘TIMEOUT ERROR
running time: 2.384 sec., time limit: 0.352 sec.
▶large1
large test, length = ~100,000✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶large2
large test, length = ~100,000✘TIMEOUT ERROR
running time: 1.884 sec., time limit: 0.416 sec.
"""