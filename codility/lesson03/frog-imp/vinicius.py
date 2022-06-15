def solution(X, Y, D):
    if X == Y:
        return 0
    if (Y-X) % D == 0:
        return (Y-X) // D
    else:
        return ((Y-X) // D)+1