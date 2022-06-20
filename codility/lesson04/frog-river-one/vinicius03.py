def solution(X,A):
    path = set(range(1,X+1))
    idxs = dict()
    if not path.issubset(set(A)):
        return -1
    else:
        for index, val in enumerate(A):
            if val not in idxs.keys():
                idxs[val] = index
            if len(idxs) == X:
                return max(idxs.values())
