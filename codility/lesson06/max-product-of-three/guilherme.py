def solution(A=[]):
    # write your code in Python 3.6
    A.sort()
    len_A = len(A)
    min_A = min(A)
    max_A = max(A)
    if len_A == 3:
        return A[0] * A[1] * A[2]

    if min_A >= 0 or max_A <= 0:
        return A[-1] * A[-2] * A[-3]

    negatives = []
    for i in range(0, 3):
        if A[i] < 0:
            negatives.append(A[i])

    positives = []
    for i in range(1, 4):
        if A[-i] > 0:
            positives.append(A[-i])

    max_product = -float('inf')

    if len(negatives) <= 1:
        max_product = positives[0] * positives[1] * positives[2]
    else:
        if len(positives) >= 3:
            max_product = max(positives[0] * positives[1] * positives[2], max_product)

        if len(negatives) >= 2:
            max_product = max(positives[0] * negatives[0] * negatives[1], max_product)

    return max_product