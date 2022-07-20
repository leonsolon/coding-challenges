#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def queue_using_two_stacks(queries):
    queue = []
    result = []
    for i, q in enumerate(queries):

        if q[0] == 1:
            queue.append(q[1])
        elif q[0] == 2:
            queue.pop(0)
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