def solution(A, K):
    if len(A) == 0:
        return A
    lista = [0] * len(A)
    for i in range(0, len(A)):
        new_index = i + (K % len(A))
        if new_index > (len(A)-1):
            new_index = new_index - len(A)
        lista[new_index] = A[i]
    return lista