# Week 1 - Array
# Product of Array Except Self
# Runtime: 331 ms, faster than 36.34% of Python online submissions for Product of Array Except Self.
# Memory Usage: 21.1 MB, less than 37.03% of Python online submissions for Product of Array Except Self.


def productExceptSelf(nums):
    
    N = len(nums)
    p_left = 1
    a_left = [1]
    for i in range(0, N-1):
      p_left = p_left * nums[i]
      a_left.append(p_left)

    #print(a_left)
    
    p_right = 1
    a_right = [1]
    for i in range(N-1, 0, -1):
      p_right = p_right * nums[i]
      a_right.append(p_right)

    a_right.reverse()
    #print(a_right)
    
    
    answer = list(map(lambda x,y: x*y, a_right, a_left))
    
    return answer


assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
