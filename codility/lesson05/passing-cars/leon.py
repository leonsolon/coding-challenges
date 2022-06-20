# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # 0 -> east
    # 1 <- west
    number_previous_east = 0
    crossing_cars = 0

    for element in A:
        # car traveling east
        if element == 0:
            number_previous_east += 1
        else:
            crossing_cars += number_previous_east
    
    if crossing_cars > 1e9:
        return -1
    else:
        return crossing_cars
