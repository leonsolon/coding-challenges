def solution(A):# O(N**2) - 100% em Correctness - 12% em Performance
    # write your code in Python 3.6
    starts = []
    ends =[]
    points = set()
    intesections = 0
    for i,a in enumerate(A):
        starts.append(i - a)
        ends.append(i + a)
        points.add(i - a)
        points.add(i + a)

    sorted_points = sorted(points)
    # print(sorted_points)

    circulos_ativos = 0
    for i, point in enumerate(sorted_points):
        qtd_start = starts.count(point)
        qtd_end = ends.count(point)
        # print(f'point: {point} - qtd_start:{qtd_start} - qtd_end:{qtd_end}')
        intesections += qtd_start*(2*circulos_ativos + qtd_start - 1)/2
        circulos_ativos += qtd_start - qtd_end


    return int(intesections)