def solution(X, A):
    # write your code in Python 3.6
    steps = set(range(1, X+1))

    for i, element in enumerate(A):
        if element in steps:
            steps.remove(element)

        if len(steps) == 0:
            return i

    return -1
