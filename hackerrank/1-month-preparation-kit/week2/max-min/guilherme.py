def maxMin(k, arr):
    arr.sort()
    len_arr = len(arr)
    min_unfairness = float('inf')
    for i, a in enumerate(arr):
        if i+k <= len_arr:
            min_arr = arr[i]
            max_arr = arr[k+i-1]
            unfairness = max_arr - min_arr
            min_unfairness = min(min_unfairness, unfairness)
    return min_unfairness
