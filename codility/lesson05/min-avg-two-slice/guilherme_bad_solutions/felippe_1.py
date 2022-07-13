# 50% de resultado
# 100% correctness
# 0% performance

from itertools import islice
from statistics import mean
def solution(A):
    min_media = max(A)
    media = 0
    position = 0
    for i in range(len(A)+1):
      for j in range(i+2, len(A)+1):
        lista = list(islice(A, i, j, 1))
        media = mean(lista)
        if media <= min_media:
          min_media = media
          position = i
    return position
