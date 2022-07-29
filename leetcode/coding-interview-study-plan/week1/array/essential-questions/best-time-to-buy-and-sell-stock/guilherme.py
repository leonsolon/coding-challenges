class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_global_profit = max(prices) - min(prices)
        min_price = float('inf')
        max_price = -float('inf')
        for i, price in enumerate(prices):

            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
            if max_profit == max_global_profit:
                return max_profit

        return max_profit