def pairs(k, arr):
    dict_sum_k = {}
    dict_diff_k = {}
    count = 0
    for i, a in enumerate(arr):
        if a in dict_sum_k:
            count += 1
        if a in dict_diff_k:
            count += 1
        dict_sum_k[a + k] = i
        dict_diff_k[a - k] = i

    return count