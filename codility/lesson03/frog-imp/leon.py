def solution(X, Y, D):
    # write your code in Python 3.6

    if X == Y:
        return 0

    jumps = (Y-X) // D

    X_after = X + (D * jumps)

    if X_after >= Y:
        return jumps
    else:
        return jumps + 1
