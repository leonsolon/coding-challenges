def solution(A):
    '''
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
    set_A = set(A)
    len_set_A = len(set_A)
    max_set_A = max(set_A)
    min_set_A = min(set_A)
    if max_set_A<=0 or min_set_A >1:
        return 1
    elif len_set_A == (max_set_A - min_set_A+1):
        return max_set_A + 1
    for i in range(1, max_set_A+1):
        if not (i in set_A):
            return i