# Lesson 6 Ex 03
# TriangleCodingTask
# 62%
# 100% correctness
# 0% performance
from itertools import combinations
def solution(A):
  for element in A:
    if element < 0:   # retirando os elementos negativos
      A.remove(element)
  if len(A) < 3:
    return 0
  triangle = 0
  for triple in combinations(A, 3):
    if triple[0] + triple[1] > triple[2] and triple[1] + triple[2] > triple[0] and triple[0] + triple[2] > triple[1]:
      triangle = 1
  return triangle
