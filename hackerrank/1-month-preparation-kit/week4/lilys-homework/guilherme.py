def swap(arr, arr_beautiful, pos):
    count_diff = 0
    i = 0
    while i < len(arr):

        a = arr[i]
        a1 = arr_beautiful[i]

        if a != a1:
            i_swap = pos[a1]
            arr[i], arr[i_swap] = arr[i_swap], arr[i]
            pos[a1] = i
            pos[a] = i_swap
            count_diff += 1
        i += 1
    return count_diff


def lilysHomework(arr):
    sorted_arr = sorted(arr)
    sorted_arr_reverse = sorted(arr, reverse=True)

    pos = {}
    for i, a in enumerate(arr):
        pos[a] = i

    result1 = swap(arr.copy(), sorted_arr, pos.copy())
    result2 = swap(arr.copy(), sorted_arr_reverse, pos.copy())

    # print(result1, result2)
    return min(result1, result2)