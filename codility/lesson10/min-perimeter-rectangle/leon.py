'''
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from functools import lru_cache


@lru_cache(maxsize=None)
def calculate_factors(number):
    factors = set()

    if number % 2 == 1:
        iteration_list = range(1, max((number // 2) + 1, 2), 2)
    else:
        iteration_list = range(1, max((number // 2) + 1, 2))

    for i in iteration_list:
        if number % i == 0:
            factors.add((i, number // i))

        if i >= number // i:
            break

    return factors


def solution(N):
    # write your code in Python 3.6

    factors = calculate_factors(N)

    min_perimeter = float('inf')

    for pair_factors in factors:
        perimeter = 2 * (pair_factors[0] + pair_factors[1])
        if perimeter < min_perimeter:
            min_perimeter = perimeter

    return min_perimeter


assert solution(30) == 22

# assert solution(128) == 8
# assert solution(127) == 2
