class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if 0 in nums:
            answer = [0] * len(nums)
            zeros = nums.count(0)
            if zeros > 1:
                return answer
            else:
                product = 1
                idx_zero = -1
                for i, n in enumerate(nums):
                    if n != 0:
                        product *= n
                    if n == 0:
                        idx_zero = i
                answer[idx_zero] = product
        else:
            product = 1
            for i, n in enumerate(nums):
                product *= n

            answer = []
            for i, n in enumerate(nums):
                answer.append(int(product * (n ** -1)))

        return answer


s = Solution()
assert s.productExceptSelf([2] * 5) == [2 ** 4] * 5
assert s.productExceptSelf([2] * 99 + [0, 0]) == [0] * 101