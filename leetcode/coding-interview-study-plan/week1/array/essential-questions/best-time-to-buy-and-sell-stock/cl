#4'

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Runtime: 1651 ms, faster than 46.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 38.55% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minn = prices[0]
        maxProfit = 0
        for p in prices:
            minn = min(p, minn)
            maxProfit = max(maxProfit, p - minn)
            
        return maxProfit
