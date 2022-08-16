def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    if len_A <=2:
        return 0

    peaks_set = set()
    for i , a in enumerate(A):
        is_peak = False
        if i !=0 and i + 1 < len_A and a > A[i-1] and a > A[i+1]:
            is_peak = True

        if is_peak:
            peaks_set.add(i)

    peaks_list = list(peaks_set)
    peaks_list.sort()


    len_peaks_list = len(peaks_list)
    flags = len_peaks_list

    if len_peaks_list == 0:
        return 0
    last_peak = peaks_list[-1]
    first_peak = peaks_list[0]
    if first_peak == last_peak:
        return 1

    while True:
        total_dist = abs(first_peak - last_peak)
        avg_dist = total_dist/(flags-1)

        if avg_dist< flags:
            flags -= 1
            avg_dist = flags
            if flags <= 0:
                return flags
            continue

        last_peak_flaged = first_peak
        flags_seted = 1
        for j, peak in enumerate( peaks_list[1:]):
            dist = abs(last_peak_flaged - peak)
            if dist >= flags:
                flags_seted += 1
                last_peak_flaged = peak
                if flags_seted >= flags:
                    return flags
        flags -= 1

    return flags

assert solution([1,2,1,5,4,4,4,4,4,5,4,5,4]) == 2

# assert solution([]) == 0
# assert solution([1]) == 0
# assert solution([2]) == 0
# assert solution([1,2]) == 0
# assert solution([1,2,1]) == 1
# assert solution([3,2,1]) == 0
# assert solution([1,2,3]) == 0
# assert solution([3,2,3]) == 0
# assert solution([1,1,2,1]) == 1
# assert solution([1,2,1,3]) == 1
# assert solution([1,3,1,2,1]) == 2
# assert solution([1,2,3,4,5]) == 0
# assert solution([1,6,3,6,5,6,5,6,3,2,6,1]) == 3
# assert solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
# assert solution([1, 5, 3, 4, 3, 4, 1, 2, 7, 4, 6, 2]) == 3
# assert solution([0,1,2,1,2]) == 1

