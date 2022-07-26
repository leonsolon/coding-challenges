def solve(arr, queries):  # Falhou em 7 dos 11 casos por performance
    len_arr = len(arr)

    result = {}
    sorted_queries = sorted(queries)
    last_min = -float('inf')
    for q in sorted_queries:
        min_value = float('inf')
        slice_arr = []
        for i, a in enumerate(arr):
            if a >= last_min:
                for k in range(1, q + 1):
                    k_min = i - q + k
                    k_max = i + k
                    if k_min >= 0 and k_max <= len(arr):
                        slice_arr = arr[k_min:k_max]

                        min_value = min(min_value, max(slice_arr))

        result[q] = min_value
        last_min = min_value

    result_list = []
    for q in queries:
        result_list.append(result[q])

    return result_list