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
    str_pilha = ''
    for i in range(len(S)):
        if S[i] in abertura:
            str_pilha += S[i]
        else:
            if S[i] == ')':
                if not str_pilha.endswith('('):
                    return 0
                else:
                    str_pilha = str_pilha[:-1]
            if S[i] == ']':
                if not str_pilha.endswith('['):
                    return 0
                else:
                    str_pilha = str_pilha[:-1]
            if S[i] == '}':
                if not str_pilha.endswith('{'):
                    return 0
                else:
                    str_pilha = str_pilha[:-1]
    if not str_pilha:
        return 1
    else:
        return 0

'''
CORRECTNESS 100%
PERFORMANCE 80%
TOTAL       87%

▶large1
simple large positive test, 100K ('s followed by 100K )'s + )(
    ✘TIMEOUT ERROR
running time: 0.368 sec., time limit: 0.336 sec.
1.0.368 s TIMEOUT ERROR, running time: 0.368 sec., time limit: 0.336 sec.
2.0.036 s OK
3.0.044 s OK

'''