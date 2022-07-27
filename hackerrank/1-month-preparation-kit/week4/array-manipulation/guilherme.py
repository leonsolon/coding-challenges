def arrayManipulation(n, queries):
    start = {}
    end = {}
    for (a, b, k) in queries:
        if a in start:
            start[a] += k
        else:
            start[a] = k

        if (b) in end:
            end[b] -= k
        else:
            end[b] = -k

    current = 0
    max_value = -float('inf')
    for i in range(1, n + 1):
        if i in start:
            current += start[i]

        max_value = max(current, max_value)

        if i in end:
            current += end[i]

    return max_value