# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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


def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    peaks = get_peaks(A)
    # print(peaks)
    len_peaks = len(peaks)
    if len(peaks) == 0:
        return 0
    max_flags = len_peaks

    last_peak = max(peaks)
    for flags in range(max_flags, 0, -1):
        flaged_peaks = 0
        last_flaged_peak = -1
        for p, peak in enumerate(peaks):
            # print(flags, p, peak)
            if p == 0 or ((peak - last_flaged_peak) >= flags):
                last_flaged_peak = peak
                flaged_peaks += 1
                if flaged_peaks == flags:
                    return flags
                if (flags - flaged_peaks) * flags > last_peak - peak:
                    break

    return 0