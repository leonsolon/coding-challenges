'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
def solution(A):
    # write your code in Python 3.6
    if len(A)==0:
        return 1
    set_A = set(A)
    min_A = min(set_A)
    max_A = max(set_A)

    if max_A <=0 or min_A>1:
        return 1
    for i in range(1,max_A+2):
        if not i in set_A:
            return i

assert solution([]) ==1
assert solution([0,-1,-2]) ==1
assert solution([2]) ==1
assert solution([1,3,4]) ==2
assert solution([1,2,3,4]) ==5
A = list(range(1,100000+1))
assert solution(A) ==100001
A = list(range(1,100000+1))
a = A.pop(56)
assert solution(A) ==a
