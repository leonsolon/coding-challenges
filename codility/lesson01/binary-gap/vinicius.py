import re

def solution(n):
    if not re.findall("1(0+)(?=1)",bin(n)[2:]):
        return 0
    else:
        return len(max(re.findall("1(0+)(?=1)",bin(n)[2:])))

