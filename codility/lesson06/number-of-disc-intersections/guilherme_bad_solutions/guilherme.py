def solution(A):# O(N**2) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    starts = []
    ends = []
    info_points = []
    set_points = set()
    intesections = 0
    for i, a in enumerate(A):
        set_points.add(i-a)
        starts.append(i-a)
        set_points.add(i+a)
        ends.append(i+a)

    starts.sort() #pontos onde os circulos se iniciam
    ends.sort() #pontos onde os circulos terminam
    set_points = sorted(set_points) #conjunto de pontos

    pos_start = 0
    pos_end = 0
    for p in set_points:
        count_start = 0
        count_end = 0
        # O while a seguir conta a quantidade de inicios de circulo no ponto p
        # como o vetor com os inicios de circulo está ordenado, a verificação começa de onde parou.
        while pos_start<len(starts) and starts[pos_start]<=p:
            # print(f'p: {p} - starts[pos_start]:{starts[pos_start]} - pos_start: {pos_start}')
            if p==starts[pos_start]:
                count_start +=1
            pos_start +=1
        # O while a seguir conta a quantidade de terminos de circulo no ponto p
        # como o vetor com os terminos de circulo está ordenado, a verificação começa de onde parou.
        while pos_end<len(ends) and ends[pos_end]<=p:

            if p==ends[pos_end]:
                count_end +=1
            pos_end +=1
        info_points.append([p,count_start, count_end])

    print(info_points)

    circulos_ativos = 0
    for info in info_points:
        #quando um circulo inicia ele faz interceção com todos os circulos ativos.
        #quando dois ou mais circulos se inicial no memos ponto
        # a quantidade de interseções a ser somada vai aumentos em 1
        # sendo assim, tempos uma PA onde:
        # a(i) = circulos ativos;
        # a(n) = circulos ativos + circulos iniciados no ponto-1;
        # n = circulos iniciados; com isso, a
        # Soma = circulos iniciados*(circulos ativos + circulos ativos + circulos iniciados - 1)/2
        # Soma = circulos iniciados*(2*circulos ativos + circulos iniciados - 1)/2
        intesections += info[1]*(2*circulos_ativos + info[1] - 1)/2
        if intesections > 10000000:
            return -1
        circulos_ativos += info[1] - info[2]

    return int(intesections)
