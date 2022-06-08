def solution(A):
    # write your code in Python 3.6

    if len(A) == 1:
        return A[0]

    element_set = set()

    for element in A:
        if element in element_set:
            element_set.remove(element)
        else:
            element_set.add(element)

    return list(element_set)[0]
