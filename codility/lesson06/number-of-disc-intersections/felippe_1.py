# Lesson 6 Ex 04
# NumberOfDiscIntersections
# 50% result
# 100% correctness
# 0% performance

def solution(A):
    max = []
    min = []
    for i, e in enumerate(A): # salvando os limites de cada disco
        max.append(i+e)
        min.append(i-e)
    discs = 0
    limits = list(zip(min, max))
    for i in range(len(limits)):
        for j in range(i+1, len(limits)):
            if limits[j][0] <= limits[i][0] <= limits[j][1] or limits[j][0] <= limits[i][1] <= limits[j][1] or limits[i][0] <= limits[j][0] <= limits[i][1] or limits[i][0] <= limits[j][1] <= limits[i][1]:
                discs += 1
                if discs >= 10_000_000:
                    return -1
    return discs
