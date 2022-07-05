def pageCount(n, p):
    if n % 2 == 0:
        n += 1
    if p % 2 == 0:
        p += 1
    page_from_1 = int((p - 1) / 2)
    page_from_p = int((n - p) / 2)
    return min(page_from_1, page_from_p)
