## Missing Integer
## solução com 88%
## timeout error

def solution(A):
  A.sort()
  B = list(filter(lambda element: element >= 0, A))
  if len(B) == 0:
    return 1
  set_B = set(B)
  last = B[-1]+1
  set_test = set(range(1, last+1))
  difference = list(set_test.difference(set_B))
  if len(set_B) == len(set_test):
    return last
  else:
    return min(list(set_test.difference(set_B)))
