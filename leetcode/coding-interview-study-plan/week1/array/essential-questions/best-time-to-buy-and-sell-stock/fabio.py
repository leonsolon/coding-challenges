'''
FUNCIONOU, MAS NÃO PASSOU NA PERFORMANCE
class Solution:
    def maxProfit(self, prices: list) -> int:
        max_profit = 0
        for i, p1 in enumerate(prices):
            for j, p2 in enumerate(prices[i+1:]):
                #print(f"i={i+1}, p1={p1} || j={j+i+1}, p2={p2} || current_profit={p2-p1} || max_profit={max_profit}")
                if p2 <= p1:
                    break
                elif p2-p1 > max_profit:
                    max_profit = p2-p1
            #print('======================================')            
        return max_profit
'''

class Solution:
    def maxProfit(self, prices: list) -> int:
        current_profit, max_profit, min_price = 0, 0, 10e5 + 1
        #print(f"price=- min_price=- current_profit={current_profit} max_profit={max_profit}")
        for price in prices:
            if price < min_price:
                min_price = price
            current_profit = price - min_price
            if max_profit < current_profit:
                max_profit = current_profit
            #print(f"price={price} min_price={min_price} current_profit={current_profit} max_profit={max_profit}")    
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1]))

# Runtime: 1044 ms, faster than 95.64% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 38.55% of Python3 online submissions for Best Time to Buy and Sell Stock.