# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    # ACGT 1234

    dict_dna = dict()

    for index, element in enumerate(S):
        if index == 0:
            dict_dna[index] = {'A':0, 'C': 0, 'G': 0, 'T': 0}
        else:
            dict_dna[index] = dict_dna[index-1].copy()
        
        if element == 'A':
            dict_dna[index]['A'] += 1
        elif element == 'C':
            dict_dna[index]['C'] += 1
        elif element == 'G':
            dict_dna[index]['G'] += 1
        else:
            dict_dna[index]['T'] += 1

    #print(dict_dna)

    answer = []

    for p, q in zip(P, Q):
        if p == q:
            if S[p] == 'A':
                answer.append(1)
                continue
            elif S[p] == 'C':
                answer.append(2)
                continue
            elif S[p] == 'G':
                answer.append(3)
                continue
            else:
                answer.append(4)
                continue

        if S[p] == 'A':
            answer.append(1)
            continue

        if dict_dna[p]['A'] != dict_dna[q]['A']:
            answer.append(1)
            continue

        if S[p] == 'C':
            answer.append(2)
            continue

        if dict_dna[p]['C'] != dict_dna[q]['C']:
            answer.append(2)
            continue

        if S[p] == 'G':
            answer.append(3)
            continue


        if dict_dna[p]['G'] != dict_dna[q]['G']:
            answer.append(3)
            continue

        if S[p] == 'T':
            answer.append(4)
            continue


        if dict_dna[p]['T'] != dict_dna[q]['T']:
            answer.append(3)
            continue

    #print(len(answer))

    return answer
