def solution(N, A):
    # write your code in Python 3.6
    global_max = 0
    current_max = 0

    counters = [0] * N

    for element in A:
        if element == N + 1:
            global_max = current_max
        else:
            # value = counters[element-1]

            if counters[element - 1] >= global_max:
                counters[element - 1] += 1
            else:
                counters[element - 1] = global_max + 1

            if counters[element - 1] > current_max:
                current_max = counters[element - 1]

    for index, element in enumerate(counters):
        if element < global_max:
            counters[index] = global_max

    return counters