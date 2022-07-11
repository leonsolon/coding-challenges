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
    if S == '':
        return 1
    par = []
    colch = []
    chave = []
    prev_el = S[0]
    for i in S:
        if i == '(':
            par += i
            prev_el = i
        elif i == '[':
            colch += i
            prev_el = i
        elif i == '{':
            chave += i
            prev_el = i
        else:
            if i == ')' and prev_el in ('(',']','}',')'):
                try:
                    par.remove('(')
                    prev_el = i
                except:
                    return 0
            elif i == ']' and prev_el in (')','[','}',']'):
                try:
                    colch.remove('[')
                    prev_el = i
                except:
                    return 0
            elif i == '}' and prev_el in (')',']','{','}'):
                try:
                    chave.remove('{')
                    prev_el = i
                except:
                    return 0
            else:
                return 0
        #print(i)
    if not par and not colch and not chave:
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
running time: 1.552 sec., time limit: 0.352 sec.
1.1.552 s TIMEOUT ERROR, running time: 1.552 sec., time limit: 0.352 sec.
2.0.036 s OK
3.0.044 s OK

'''


