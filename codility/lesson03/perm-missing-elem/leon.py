def solution(A):
    # write your code in Python 3.6
    max_value = len(A) + 1

    values_set = set(range(1,max_value+1))

    for element in A:
        values_set.remove(element)

    return values_set.pop()
