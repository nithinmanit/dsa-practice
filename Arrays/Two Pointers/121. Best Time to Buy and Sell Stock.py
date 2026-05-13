class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices:
            if i > buy:
                profit = max(i-buy,profit)
            if i < buy:
                buy = i
        return profit