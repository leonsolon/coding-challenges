# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
def simple_text_editor(queries):
    s = ''
    last_s = []
    result = []
    for i, q in enumerate(queries):
        if q[0] == '1':
            last_s.append(s)
            s += q[1]
        elif q[0] == '2':
            last_s.append(s)
            s = s[:-int(q[1])]
        elif q[0] == '3':
            idx = int(q[1])-1
            result.append(s[idx])
        elif q[0] == '4':
            s = last_s.pop()
        # print('s', s)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    Q = int(input().strip())
    queries = []
    for i in range(0,Q):
        queries.append(input().strip().split())
    # print(queries)
    result = simple_text_editor(queries)
    for s in result:
        fptr.write(s)
        fptr.write('\n')