def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    min_avg = float('inf')
    start_pos = -1
    for i, a in enumerate(A):
        if i+1< len_A:
            avg_2 = (a + A[i+1])/2
            if avg_2 < min_avg:
                min_avg = avg_2
                start_pos = i
        if i+2 < len_A:
            avg_3 = (a + A[i+1] + A[i+2])/3
            if avg_3 < min_avg:
                min_avg = avg_3
                start_pos = i

    return start_pos