# Lesson 6 Ex 03
# TriangleCodingTask
# 100%

def solution(A):
  B = list(filter(lambda element: element >= 0, A)) # filtrando os valores negativos de forma mais eficiente
  if len(B) < 3:
    return 0
  B = sorted(B)
  triangle = 0
  for i in reversed(range(2, len(B))):
    if B[i] + B[i-1] > B[i-2] and B[i-2] + B[i-1] > B[i] and B[i] + B[i-2] > B[i-1]:
      triangle = 1
  return triangle
