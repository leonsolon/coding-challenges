def solution(N):
    binary_representantion = bin(N)[2:]

    gaps = binary_representantion.split('1')

    gaps = gaps[1:-1]

    if len(gaps) == 0:
        return 0

    max_gap = max(gaps, key=len)

    return len(max_gap)
