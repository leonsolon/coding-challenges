def hackerlandRadioTransmitters(x, k):
    min_coverage = float('inf')
    max_coverage = -float('inf')
    count_transmitters = 0
    x.sort()
    len_x = len(x)
    for i, el in enumerate(x):
        if el >= min_coverage and el <= max_coverage:
            pass
        else:
            j = 0
            while (i + j) < len_x and el + k >= x[i + j]:
                j += 1
            j -= 1
            min_coverage = x[i + j] - k
            max_coverage = x[i + j] + k
            count_transmitters += 1
            print(i + j, j, min_coverage, max_coverage)

    return count_transmitters