def solution(A): # O(N) - 100% em Correctness - 100% em Performance
    # [a, b, c, d]
    # Médias possíveis
    # 1: (a + b) / 2
    # 2: (b + c) / 2
    # 3: (c + d) / 2
    # 4: (a + b + c) / 3
    # 5: (b + c + d) / 3
    # 6: (a + b + c + d) / 4
    # supondo que a menor média seja a 6.
    # para isso "(a + b + c + d) / 4" deve ser menor que "(a + b) / 2"
    # isso só acontece se "(c + d) / 2" for menor que "(a + b + c + d) / 4" o que é impossível
    # com isso a menor média pode ter no máximo 3 elementos

    # write your code in Python 3.6
    len_A = len(A)
    minimal_avg = max(A)
    minimal_p = 0

    if len(set(A))==1:
        return 0

    for i in range(0, len_A-1):
        j = i+1
        k = i+2
        soma = A[i]+A[j]
        avg = (soma)/2
        if k < len_A and A[k]<avg :
            avg = (soma + A[k])/3

        if avg < minimal_avg:
            minimal_p = i
            minimal_avg = avg
    return minimal_p

print(solution([10, 10, -1, 2, 3, 2, -1, 5, 10, -1, 2, -1, 2, -1, 1 ]))
print(solution([1,2,3,4,5,6,7,8,9,10]))
print(solution([10,9,8,7,6,5,4,3,2,1]))
print(solution([10, 10, -1, 2, 4, -1, 2, -1]))
print(solution([4, 2, 2, 5, 1,5,8]))
print(solution([-3, -5, -8, -4, -10]))
print(solution( [-10000, -10000]))