def minimumBribes(q):
    j = len(q)
    i = j - 1
    count_bribes = count_bribes_person = 0

    while i >= 0:

        if q[i] == j:

            if count_bribes_person > 2:
                print('Too chaotic')
                break
            count_bribes_person = 0
            # print(j, i, q[i], q)
            if j != i + 1:
                aux = q[i]
                for k in range(i, j - 1):
                    q[k] = q[k + 1]
                q[j - 1] = aux
            # print(q)
            j -= 1
            i = j - 1
            q[i]
        else:
            i -= 1
            count_bribes += 1
            count_bribes_person += 1
            # print(j ,i, q[i], count_bribes)
    else:
        print(count_bribes)