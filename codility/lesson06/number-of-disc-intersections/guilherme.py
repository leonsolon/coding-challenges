# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 0:
        return 0
    starts = {}
    ends = {}
    pos = set()
    for i, a in enumerate(A):
        start = i - a
        end = i + a
        pos.add(start)
        pos.add(end)
        if start in starts:
            starts[start] += 1
        else:
            starts[start] = 1

        if end in ends:
            ends[end] += 1
        else:
            ends[end] = 1

    # print(starts, ends)

    pos_list = list(pos)
    pos_list.sort()

    open_disc = 0
    intersecting_disc = 0
    for i, p in enumerate(pos_list):
        if p in starts:
            intersecting_disc += (2 * open_disc + starts[p] - 1) * starts[p] / 2
            if intersecting_disc > 10000000:
                return -1
            open_disc += starts[p]
        if p in ends:
            open_disc -= ends[p]

    return int(intersecting_disc)