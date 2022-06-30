def get_sum_slice(A):
    current_sum = 0
    sum_slices = []
    for i, a in enumerate(A):
        current_sum = max(a, a + current_sum,0)
        sum_slices.append(current_sum)
    return sum_slices

def solution(A):
    # write your code in Python 3.6
    A = A[1:-1]
    sum_slice_left = [0] + get_sum_slice(A)
    sum_slice_right = [0] + get_sum_slice(A[::-1])
    sum_slice_right = sum_slice_right[::-1]
    print(sum_slice_left, sum_slice_right)
    print(sum_slice_left[:-1], sum_slice_right[1:])
    sum_slice = zip(sum_slice_left[:-1], sum_slice_right[1:])
    max_sum = 0
    for i, (sum_left,sum_right) in enumerate(sum_slice):
        max_sum = max(max_sum, sum_left+sum_right)

    return max_sum

print(solution([0, 10, -5, -2, 0]))
print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
