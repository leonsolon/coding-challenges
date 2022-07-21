# Lesson 7 Ex 02
# Fish
# 75%
# correctness 100%
# performance 50%
# Detected time complexity: O(N ** 2)


def solution(A, B):
    if len(A) == 1:
        return 1
    if sum(B) == 0 or sum(B) == len(B):
        return len(B)
    N = len(A)
    k = 0
    
    while k < N - 1:
  
        if B[k] == 1 and B[k+1] == 0:
            if A[k] > A[k+1]: # peixe 1 comeu o peixe 0
                A.pop(k+1)
                B.pop(k+1)
                k = 0
                N = len(A)
            else:  # peixe 0 comeu o peixe 1
                A.pop(k)
                B.pop(k)
                k = 0
                N = len(A)
        else:
            k +=1

    return len(A)
