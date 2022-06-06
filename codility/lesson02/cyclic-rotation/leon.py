def solution(A, K):
    # write your code in Python 3.6
    len_A = len(A)

    if len_A in [0, 1]:
        return A

    module_AK = K % len_A

    if module_AK == 0:
        return A

    first_part = A[-module_AK:]
    second_part = A[:-module_AK]


    return first_part + second_part

