def miniMaxSum(arr):
    min_arr = min(arr)
    max_arr = max(arr)
    sum_arr = sum(arr)
    min_sum_4_values = sum_arr - max_arr
    max_sum_4_values = sum_arr - min_arr
    print(min_sum_4_values, max_sum_4_values)