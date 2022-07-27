def equalStacks(h1, h2, h3):
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    while True:
        max_h = max(sum_h1, sum_h2, sum_h3)
        min_h = min(sum_h1, sum_h2, sum_h3)

        if max_h == 0:
            return 0
        if sum(h1) == sum(h2) and sum(h1) == sum(h3):
            return sum(h1)

        while sum_h1 > min_h:
            sum_h1 -= h1.pop()
            # print('h1', h1, sum_h1)
        while sum_h2 > min_h:
            sum_h2 -= h2.pop()
            # print('h2', h2, sum_h2)
        while sum_h3 > min_h:
            sum_h3 -= h3.pop()
            # print('h3', h3, sum_h3)