class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = -float('inf')
        i = 0
        j = len(height) - 1
        while i <= j:
            h1 = height[i]
            h2 = height[j]
            vol = (j - i) * min(h1, h2)
            # print(i, j, h1, h2,j-i, vol)
            max_vol = max(max_vol, vol)
            if h1 < h2:
                i += 1
            else:
                j -= 1

        return max_vol