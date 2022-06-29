'''
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. 
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires 
you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P and Q is an integer within the range [0..N - 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
'''
def pref_sums(S):
    str_list = list(S)
    aux = ['']*(len(S)+1)
    for i in range(1,(len(S)+1)):
        aux[i] = aux[i-1] + str_list[i-1] #MEMORY ERROR - TAMBÉM TEVE PROBLEMA DE CORRECTNESS
    return aux[1:]

def result_slice(aux, p, q):
    if p == q:
        return aux[q][-1]
    if p == 0:
        return aux[q]
    return aux[q].replace(aux[p],'',1)

def solution(S, P, Q):
    aux = pref_sums(S)
    list_of_mins = []
    dict_vals = {
        'A':1,
        'C':2,
        'G':3,
        'T':4
    }
    for p,q in zip(P,Q):
        result = result_slice(aux, p, q)
        if 'A' in result:
            list_of_mins.append(1)
        elif 'C' in result:
            list_of_mins.append(2)
        elif 'G' in result:
            list_of_mins.append(3)
        elif 'T' in result:
            list_of_mins.append(4)
        else:
            list_of_mins.append(dict_vals[aux[p]])
    return list_of_mins


#PERFORMANCE RUIM TB
# def pref_sums_A(S):
#     num_str = S.replace('A', '1').replace('C', '0').replace('G', '0').replace('T','0')
#     list_of_ints = [int(x) for x in list(num_str)]
#     aux = [0]*(len(S)+1)
#     for i in range(1,(len(S)+1)):
#         aux[i] = list_of_ints[i-1] + aux[i-1]
#     return aux[1:]

# def pref_sums_C(S):
#     num_str = S.replace('A', '0').replace('C', '1').replace('G', '0').replace('T','0')
#     list_of_ints = [int(x) for x in list(num_str)]
#     aux = [0]*(len(S)+1)
#     for i in range(1,(len(S)+1)):
#         aux[i] = list_of_ints[i-1] + aux[i-1]
#     return aux[1:]

# def pref_sums_G(S):
#     num_str = S.replace('A', '0').replace('C', '0').replace('G', '1').replace('T','0')
#     list_of_ints = [int(x) for x in list(num_str)]
#     aux = [0]*(len(S)+1)
#     for i in range(1,(len(S)+1)):
#         aux[i] = list_of_ints[i-1] + aux[i-1]
#     return aux[1:]

# def pref_sums_T(S):
#     num_str = S.replace('A', '0').replace('C', '0').replace('G', '0').replace('T','1')
#     list_of_ints = [int(x) for x in list(num_str)]
#     aux = [0]*(len(S)+1)
#     for i in range(1,(len(S)+1)):
#         aux[i] = list_of_ints[i-1] + aux[i-1]
#     return aux[1:]

# def sums(aux, p, q):
#     return aux[q] - aux[p]

# def solution(S, P, Q):
#     S_A = pref_sums_A(S)
#     S_C = pref_sums_C(S)
#     S_G = pref_sums_G(S)
#     #S_T = pref_sums_T(S)
#     list_of_mins = []
#     for p,q in zip(P,Q):
#         sumsA = sums(S_A, p, q)
#         sumsC = sums(S_C, p, q)
#         sumsG = sums(S_G, p, q)
#         #sumsT = sums(S_T, p, q)
#         if sumsA > 0:
#             list_of_mins.append(1)
#         elif sumsC > 0:
#             list_of_mins.append(2)
#         elif sumsG > 0:
#             list_of_mins.append(3)
#         else:
#             list_of_mins.append(4)
#     return list_of_mins
