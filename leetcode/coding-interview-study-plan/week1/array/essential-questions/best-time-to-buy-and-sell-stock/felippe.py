# Week 1 - Array
# Best Time to Buy and Sell Stock
# Runtime: 1805 ms, faster than 6.32% of Python online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 22.8 MB, less than 30.34% of Python online submissions for Best Time to Buy and Sell Stock.

def maxProfit(prices):
       
  N = len(prices)
  minimo = float('inf')
  max_profit = -float('inf')

  for i in range(N):
    minimo = min(minimo, prices[i])
    profit = prices[i] - minimo
    max_profit = max(max_profit, profit)
      
  return max(0, max_profit)

assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([7,6,4,3,1]) == 0
