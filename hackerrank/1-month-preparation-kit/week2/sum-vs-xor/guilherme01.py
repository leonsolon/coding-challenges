# Não passa em 4 testes por performance
def sumXor(n):
    # Write your code here
    count =0
    for x in range(0,n+1):
        if x+n == x^n:
            count+=1
    return count