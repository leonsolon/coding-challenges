def solution(A):
    len_A = len(A)
    if len_A<3:
        return 0
    if max(A)<0:
        return 0

    sorted_A = sorted(A)
    sorted_positive_A = []
    for i, a in enumerate(sorted_A):
        if a>=0:
            sorted_positive_A = sorted_A[i:]
            break

    len_sorted_positive_A = len(sorted_positive_A)
    if len_sorted_positive_A<3:
        return 0

    for i,a in enumerate(sorted_positive_A):
        if i> 0 and i<len_sorted_positive_A-1:
            max_part_1 = max(sorted_positive_A[0:i])
            min_part_2 = min(sorted_positive_A[i+1:])
            if a > min_part_2 - max_part_1:
                return 1

    return 0