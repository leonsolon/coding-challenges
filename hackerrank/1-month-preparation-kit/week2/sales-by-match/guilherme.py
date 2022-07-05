from collections import Counter


def sockMerchant(n, ar):
    if len(ar) == 0:
        return 0
    count_ar = Counter(ar)

    pairs = 0
    for key, value in count_ar.items():
        pairs += value // 2