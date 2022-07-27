def maxSubarray(arr):
    sum_sub_seq = 0
    sum_sub_arr = 0
    max_sub_arr = -float('inf')
    max_arr = max(arr)
    if max_arr < 0:
        sum_sub_seq = max_arr

    for i, a in enumerate(arr):
        sum_sub_arr = max(a, sum_sub_arr + a)
        max_sub_arr = max(sum_sub_arr, max_sub_arr)
        if a > 0:
            sum_sub_seq += a
    return [max_sub_arr, sum_sub_seq]