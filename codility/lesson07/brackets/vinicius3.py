'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
'''

def solution(S):
    if len(S) == 0:
        return 1
    if len(S) % 2 != 0:
        return 0
    if S.count('{') != S.count('}') or S.count('[') != S.count(']') or S.count('(') != S.count(')'):
        return 0
    if S.endswith('{') or S.endswith('[') or S.endswith('('):
        return 0
    if S.startswith('}') or S.startswith(']') or S.startswith(')'):
        return 0
    abertura = '{[('
    pilha = []
    for i in S:
        if i in abertura:
            pilha += i
        else:
            if i == ')':
                if not pilha:
                    return 0
                if pilha[-1] != '(':
                    return 0
                else:
                    pilha.pop()
            if i == ']':
                if not pilha:
                    return 0
                if pilha[-1] != '[':
                    return 0
                else:
                    pilha.pop()
            if i == '}':
                if not pilha:
                    return 0
                if pilha[-1] != '{':
                    return 0
                else:
                    pilha.pop()
    if not pilha:
        return 1
    else:
        return 0

'''
TOTAL 100%
'''