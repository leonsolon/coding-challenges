# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
from collections import deque


def queue_using_two_stacks(queries):
    queue = deque()
    result = []
    for q in queries:
        if q[0] == 1:
            queue.append(q[1])
        elif q[0] == 2:
            queue.popleft()
        elif q[0] == 3:
            result.append(queue[0])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n_queries = int(input().strip())
    queries = []
    for i in range(0, n_queries):
        querie_string = input().split()
        querie = []
        for q in querie_string:
            querie.append(int(q))
        queries.append(querie)

    result = queue_using_two_stacks(queries)

    for r in result:
        fptr.write(str(r))
        fptr.write('\n')

    fptr.close()