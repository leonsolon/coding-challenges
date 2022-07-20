# Lesson 6 Ex 03
# TriangleCodingTask
# 81%
# 100% correctness
# 50% performance
# memory error ao gerar as combinações
from itertools import combinations
def solution(A):
  B = list(filter(lambda element: element >= 0, A)) # filtrando os valores negativos de forma mais eficiente
  if len(B) < 3:
    return 0
  triples = list(combinations(B, 3))
  triangle = 0
  for triple in triples:
    if triple[0] + triple[1] > triple[2] and triple[1] + triple[2] > triple[0] and triple[0] + triple[2] > triple[1]:
      triangle = 1
  return triangle
