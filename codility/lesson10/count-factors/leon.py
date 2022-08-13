'''
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from functools import lru_cache


@lru_cache(maxsize=None)
def factors(number):
    factors = set()

    if number % 2 == 1:
        iteration_list = range(1, max((number // 2) + 1, 2), 2)
    else:
        iteration_list = range(1, max((number // 2) + 1, 2))

    for i in iteration_list:
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)

        if i >= number // i:
            break

    return factors


def solution(N):
    # write your code in Python 3.6
    return len(factors(N))


assert solution(1) == 1
assert solution(2) == 2
assert solution(3) == 2
assert solution(4) == 3
assert solution(24) == 8
assert solution(128) == 8
assert solution(127) == 2
