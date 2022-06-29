def solution(S, P, Q):
    # write your code in Python 3.6

    answers =[]
    for i, (p,q) in enumerate(zip(P,Q)):
        slice = S[p:q+1]
        if 'A' in slice:
            answers.append(1)
        elif 'C' in slice:
            answers.append(2)
        elif 'G' in slice:
            answers.append(3)
        elif 'T' in slice:
            answers.append(4)
    return answers