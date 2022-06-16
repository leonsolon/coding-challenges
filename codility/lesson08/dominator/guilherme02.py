def solution(A=[]): # O(N*log(N)) or O(N) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    len_A = len(A)
    set_A = set(A)
    len_set_A = len(set_A)
    A_sorted = sorted(A)

    if len_set_A==1:
        return 0
    elif len_set_A==0:
        return -1
    else:
        last_a = None
        count_a = 1
        for i,a in enumerate(A_sorted):

            if a==last_a:
                count_a +=1
                if count_a > len_A / 2:
                    return A.index(a)
            else:
                count_a = 1
            last_a = a
            if (len_A) - i + count_a < len_A / 2:
                return -1
    return -1

print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
print(solution([2,2,2,3,3,3,4,4,4]))