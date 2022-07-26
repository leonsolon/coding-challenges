# Lesson 7 Ex 03
# Nesting
# 100%

def solution(S):
    stack = 0
    open_str = '({['
    close_str = ')}]'
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']

    if len(S) % 2 != 0: # testando para número ímpar de strings
        return 0

    for element in S:
        if element == '(':
            stack += 1   # soma as aberturas
        if element == ')':
            if stack == 0:   # testa se há um bracket de fechamento antes de um abertura
                return 0
            stack -= 1 # subtrai os fechamentos
    if stack == 0:
        return 1
    else:
        return 0
