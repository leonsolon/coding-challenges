# Lesson 10 EX 02
# MinPerimeterRectangle
# 100%

def solution(N):

  min_perim = float('inf')
  i = 1
  
  while (i * i <= N): 
    if (N % i == 0):
      min_perim = min(min_perim, 2*(N//i + i))
    i += 1
    
  return min_perim
