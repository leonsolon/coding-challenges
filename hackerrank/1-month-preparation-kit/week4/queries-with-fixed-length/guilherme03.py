def solve(arr, queries): # Falhou em 10 dos 12 casos por performance
    max_querie = max(queries)
    new_arr = []
    result = []
    for j in range(1, max_querie + 1):
        if j != 1:
            for i, a in enumerate(arr):
                if i + 1 < len(arr):
                    new_arr.append(max(a, arr[i + 1]))
            arr = new_arr
            new_arr = []

        # print(j, arr)
        if j in queries:
            result.append(min(arr))

    return result