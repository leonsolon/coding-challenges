def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    answer_arr = []
    answer_arr.index()
    arr = []
    for i in range(0,n):
        arr.append([])

    for (tipo, x, y) in queries:
        idx = (x^last_answer) % n
        if tipo ==1:
            arr[idx].append(y)
        else:
            idx2 = y % len(arr[idx])
            last_answer = arr[idx][idx2]
            answer_arr.append(last_answer)
    return answer_arr