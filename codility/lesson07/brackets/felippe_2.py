# Lesson 7 Ex 01
# Brackets
# 100%

def solution(S):
    stack = []
    open_str = '({['
    close_str = ')}]'
    open_list = ['(', '{', '[']
    close_list = [')', '}', ']']

    if len(S) % 2 != 0: # testando para número ímpar de strings
        return 0

    for element in S:
        if element in open_str:
            stack.append(open_list.index(element))    # salva o index do bracket de abertura
        if element in close_str:
            if len(stack) == 0:   # testa se há um bracket de fechamento antes de um abertura
                return 0
            if close_list.index(element) == stack[-1]: # compara para ver se o tipo de bracket é o mesmo
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
