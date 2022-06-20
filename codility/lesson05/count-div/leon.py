# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6

    # In case A == B
    if (A == B):
        if A % K == 0:
            return 1
        else:
            return 0

    if (A > 0) & (A < K):
        A = K

    mod_A = A % K
    mod_B = B % K

    diff = B - A

    number_divisors = diff // K

    if (mod_A == 0) | (mod_B == 0):
        number_divisors += 1


    return number_divisors
