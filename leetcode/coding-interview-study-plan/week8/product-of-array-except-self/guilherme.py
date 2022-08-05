class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        zeros = nums.count(0)
        if zeros >= 2:
            return [0] * len(nums)
        else:
            product = 1
            zero_pos = -1
            for i, num in enumerate(nums):
                if num != 0:
                    product *= num
                else:
                    zero_pos = i
            if zeros == 1:
                answer[zero_pos] = product
            else:

                for i, num in enumerate(nums):
                    answer[i] = int(product * (num ** -1))

        return answer
