# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    ones = sum(A)
    zeros = len_A - ones
    total_passing_cars = 0
    passing_cars = ones


    for a in A:
        if a == 0:
            total_passing_cars += passing_cars
            if total_passing_cars >1000000000:
                return -1
        else:
            passing_cars -= 1

    return total_passing_cars

