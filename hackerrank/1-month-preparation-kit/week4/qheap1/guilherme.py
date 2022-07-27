# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import heapq
def qheap1(queries):
    heap = []
    result = []
    need_heapfy = False
    for i, q in enumerate(queries):
        if q[0] == '1':
            heapq.heappush(heap, int(q[1]))
        elif q[0] == '2':
            heap.remove(int(q[1]))
            need_heapfy = True
        elif q[0] == '3':
            if need_heapfy:
                heapq.heapify(heap)
                need_heapfy = False
            result.append(str(heap[0]))
    return result




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    Q = int(input().strip())
    queries = []
    for i in range(0,Q):
        queries.append(input().strip().split())
    # print(queries)
    result = qheap1(queries)
    for s in result:
        fptr.write(s)
        fptr.write('\n')
