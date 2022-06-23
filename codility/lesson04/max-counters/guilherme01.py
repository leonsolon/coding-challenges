'''
    You are given N counters, initially set to 0, and you have two possible operations on them:

    increase(X) − counter X is increased by 1,
    max counter − all counters are set to the maximum value of any counter.
    A non-empty array A of M integers is given. This array represents consecutive operations:

    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
    For example, given integer N = 5 and array A such that:

        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the values of the counters after each consecutive operation will be:

        (0, 0, 1, 0, 0)
        (0, 0, 1, 1, 0)
        (0, 0, 1, 2, 0)
        (2, 2, 2, 2, 2)
        (3, 2, 2, 2, 2)
        (3, 2, 2, 3, 2)
        (3, 2, 2, 4, 2)
    The goal is to calculate the value of every counter after all operations.

    Write a function:

    def solution(N, A)

    that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

    Result array should be returned as an array of integers.

    For example, given:

        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the function should return [3, 2, 2, 4, 2], as explained above.

    Write an efficient algorithm for the following assumptions:

    N and M are integers within the range [1..100,000];
    each element of array A is an integer within the range [1..N + 1].
'''
def solution(N, A=[]): # O(N + M) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    count_sub_A = {}
    max_counter = 0
    for a in A:
        if a == N + 1:
            if len(count_sub_A) > 0:
                max_counter += max(count_sub_A.items(), key=lambda x: x[1])[1]
                count_sub_A = {}
        else:
            if a in count_sub_A:
                count_sub_A[a]+=1
            else:
                count_sub_A[a] = 1
    else:
        max_counter_list = [max_counter] * N
        for k,a in count_sub_A.items():
            max_counter_list[k - 1] += a

    return max_counter_list