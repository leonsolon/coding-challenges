# Week 1
# Recursion
# Generate Parentheses
# Runtime: 89 ms, faster than 9.60% of Python online submissions for Generate Parentheses.
# Memory Usage: 13.5 MB, less than 96.96% of Python online submissions for Generate Parentheses.

from itertools import product
def generateParenthesis(n):
    
    
    s = product('()', repeat = n*2)
    output =[]
           
    
    for t in s:
      #print(t)
      stack = 0
      s =""
      for e in t:
        #print(e)
        if e == '(':
            s += e
            stack += 1   # soma as aberturas
        if e == ')':
            if stack == 0:   # testa se há um bracket de fechamento antes de um abertura
                break
            s += e
            stack -= 1 # subtrai os fechamentos
        if stack == 0:
          if len(s) == n*2:
            output.append(s)
    
    
    return output
