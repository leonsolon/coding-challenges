'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''

def solution(A):
    if len(A) == 1:
        return 0
    if len(A) == 2:
        if A[0] == A[1]:
            return 1
        else:
            return 0
    from collections import Counter
    leader_freq = len(A) // 2
    leader = float('inf')
    qt_equileaders = 0
    countdict = Counter(A)
    for number, count in countdict.items():
        if count > leader_freq:
            leader = number
            break
    if leader == float('inf'):
        return 0
    else:
        arr = [0]*len(A)
        for index, val in enumerate(A):
            if val == leader:
                arr[index] = 1
        pref_sums = [0]*(len(A)+1)
        for i in range(1,len(arr)+1):
            pref_sums[i] = arr[i-1] + pref_sums[i-1]
        pref_sums = pref_sums[1:]
        for index, val in enumerate(pref_sums):
            if index < len(pref_sums)-1: #retira o último elemento do prefix sums.   
                if val/(index + 1) > 0.5 and (pref_sums[-1] - val)/(len(pref_sums)-1-index) > 0.5:
                    qt_equileaders +=1
        return qt_equileaders

'''
CORRECTNESS 100%
PERFORMANCE 100%
TOTAL       100%
'''