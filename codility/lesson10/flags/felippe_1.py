# Lesson 10 EX 03
# Flags
# 73%
# 100% correctness
# 42% performance: timeout
# Detected time complexity: O(N * sqrt(N))

def solution(A):
  
  N = len(A)
  
  # finding the peaks
  
  peaks = [0] * N
  
  for i in range(1, N - 1):
    if A[i] > A[i-1] and A[i] > A[i+1]:
      peaks[i] = 1 # marking the peaks with 1
  
  if sum(peaks) == 0: # there are no peaks
    return 0

  if sum(peaks) == 1: # there are only one peak
    return 1

  #print(peaks)  
  
  # finding the number of flags
  
  for k in range(sum(peaks), 0, -1):
    flags = k # maximum number of flags 
    i = 0 
    while i < N and flags > 0:
      if peaks[i] == 1: # there is a peak!
        flags -= 1 # a flag is placed
        i += k # jump the distance
      else:
        i += 1 # jump to next index
    if flags == 0: # all flags are placed
      return k
  
  return 1 # safety return
