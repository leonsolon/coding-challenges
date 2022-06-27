def solution(A):
  A.sort()
  B = list(filter(lambda element: element >= 0, A))
  if len(B) == 0:
    return 1
  set_B = set(B)
  set_test = set(range(1, B[-1]+2))
  if len(set_B) == len(set_test):
    return B[-1]+1
  else:
    return min(list(set_test.difference(set_B)))
