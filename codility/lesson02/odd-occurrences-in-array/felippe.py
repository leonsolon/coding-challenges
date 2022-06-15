from collections import Counter
def solution(A):
    occurrences = list(Counter(A).items())
    for key, value in occurrences:
      if value % 2 == 1:
        return int(key)
        break
