def solve(arr, queries): # Falhou em 8 dos 11 casos por performance
    len_arr = len(arr)

    result = []
    for q in queries:
        min_value = float('inf')
        slice_arr = []
        for i, a in enumerate(arr):
            if i < q:
                slice_arr.append(a)
                if len(slice_arr) == q:
                    min_value = min(min_value, max(slice_arr))
            else:
                slice_arr.pop(0)
                slice_arr.append(a)
                min_value = min(min_value, max(slice_arr))

        result.append(min_value)

    return result




