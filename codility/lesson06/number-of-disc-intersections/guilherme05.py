def solution(A):# O(N**2) - 100% em Correctness - 25% em Performance
    # write your code in Python 3.6
    starts = []
    ends =[]

    points = set()
    intesections = 0
    len_A = len(A)
    for i,a in enumerate(A):
        points.add(i - a)
        points.add(i + a)

    sorted_points = sorted(points)
    qtd_starts = [0]*len(points)
    qtd_ends = [0]*len(points)

    for i, a in enumerate(A):
        qtd_starts[sorted_points.index(i-a)] +=1
        qtd_ends[sorted_points.index(i+a)] += 1



    circulos_ativos = 0
    for i, point in enumerate(sorted_points):
        # print(f'point: {point} - qtd_start:{qtd_start} - qtd_end:{qtd_end}')
        intesections += qtd_starts[i]*(2*circulos_ativos + qtd_starts[i] - 1)/2
        if intesections > 10000000:
            return -1
        circulos_ativos += qtd_starts[i] - qtd_ends[i]

    return int(intesections)