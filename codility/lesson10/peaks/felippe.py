def solution(A):

  # finding the peaks

  N = len(A)
  peaks = []
  
  for i in range(1, N - 1):
    if A[i] > A[i-1] and A[i] > A[i+1]:
      peaks.append(i)
  
  if len(peaks) == 0: # there are no peaks
    return 0

  if len(peaks) == 1: # there are only one peak
    return 1

  # finding the factors for dividing A

  count = 0
  j = 1
  factors = []
  
  while (j * j < N): 
    if (N % j == 0):
      factors.append(j)
      factors.append(N//j)
    j += 1
  if (j * j == N): 
    factors.append(j)
  
  factors.sort()
    
  # finding the maximum number of blocks
  
  nr_blocks = [N//factors[i] for i in range(len(factors))] 
  nr_blocks = list(filter(lambda x: x <= len(peaks), nr_blocks)) # the number of blocks must be smaller than or equal to the numbers of peaks
  
  set_peaks = set(peaks)
  size = 0
  result = 1
  count = 0
  
  for blocks in nr_blocks:
    size = N//blocks # size of each block
    for k in range(0, blocks):
      set_test = set(range(size*k, size*(k+1))) # setting the block
      if len(set_test.intersection(set_peaks)) > 0: # there is, at least, one peak in the block
        count += 1
    if count == blocks:
      return blocks
    else:
      count = 0

  return result
