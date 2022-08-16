class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        collor_list = [0] * 3
        for n in nums:
            collor_list[n] += 1

        # print(collor_list)

        k = 0
        for collor, n in enumerate(collor_list):
            for j in range(0, n):
                nums[k] = collor
                k += 1

