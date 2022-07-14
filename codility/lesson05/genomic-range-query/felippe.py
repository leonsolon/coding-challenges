def solution(S, P, Q):

  impact = []
  for i in range(len(P)):
    query = (S[P[i]:Q[i]+1])
    if 'A' in query:
      impact.append(1)
    elif 'C' in query:
      impact.append(2) 
    elif 'G' in query:
      impact.append(3)
    elif 'T' in query:
      impact.append(4)
  return impact 
