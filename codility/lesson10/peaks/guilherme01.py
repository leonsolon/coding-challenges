def get_peaks(A):
    len_A = len(A)
    peaks = []
    for i, a in enumerate(A):
        if i == 0 or i == len_A - 1:
            pass
        else:
            if a > A[i - 1] and a > A[i + 1]:
                peaks.append(i)
    return peaks


def get_factors(N, max_factor):
    i = 1
    sqr_N = N ** (1 / 2)
    factors = []
    while i <= sqr_N and i <= max_factor:
        if N % i == 0:
            if i <= max_factor:
                factors.append(i)
            if N / i <= max_factor:
                factors.append(int(N / i))

        i += 1
    return factors


def solution(A): # O(N * log(log(N))) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    # print(A)
    len_A = len(A)
    if min(A) == max(A):
        return 0

    if len_A <= 2:
        return 0

    peaks = get_peaks(A)
    # print(peaks)
    len_peaks = len(peaks)
    if len_peaks == 0:
        return 0

    factors = get_factors(len_A, len_peaks)
    # print(len_A,len_peaks)
    factors.sort(reverse=True)
    # print(factors)

    for i, factor in enumerate(factors):
        peaked_block = 0
        size_block = len_A / factor
        for peak in peaks:
            # print(peak, peaked_block*size_block, (peaked_block+1)*size_block)
            if peak >= peaked_block * size_block and peak < (peaked_block + 1) * size_block:
                peaked_block += 1
                if peaked_block == factor:
                    return int(factor)

    return 0