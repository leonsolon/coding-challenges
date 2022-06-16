def solution(A=[]): # O(N*log(N)) or O(N) or O(N**2) - 100% em Correctness - 50% em Performance
    # write your code in Python 3.6
    len_A = len(A)
    set_A = set(A)
    len_set_A = len(set_A)

    if len_set_A==1:
        return 0
    elif len_set_A==0:
        return -1
    else:
        for a in set_A:
            count_a = A.count(a)
            if count_a > len_A/2:
                return A.index(a)
            elif count_a == len_A/2:
                return -1
    return -1