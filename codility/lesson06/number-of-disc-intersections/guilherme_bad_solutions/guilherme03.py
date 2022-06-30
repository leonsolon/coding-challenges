def solution(A):# O(N**2) - 100% em Correctness - 25% em Performance
    # write your code in Python 3.6
    starts = []
    ends =[]
    points = set()
    intesections = 0
    len_A = len(A)
    for i,a in enumerate(A):
        starts.append(i - a)
        ends.append(i + a)
        points.add(i - a)
        points.add(i + a)

    sorted_points = sorted(points)
    # print(sorted_points)

    circulos_ativos = 0
    for i, point in enumerate(sorted_points):
        while point in starts:
            intesections += circulos_ativos
            starts.remove(point)
            circulos_ativos += 1
            # print(f'point: {point} - circulos_ativos:{circulos_ativos}')
        while point in ends:
            circulos_ativos -= 1
            ends.remove(point)

    return intesections