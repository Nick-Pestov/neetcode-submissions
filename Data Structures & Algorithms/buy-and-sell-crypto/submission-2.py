class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = j = profit = 0
        n = len(prices)
        while i < n:
            while j + 1 < n and prices[j] < prices[j + 1]:
                j += 1
            profit = max(profit, prices[j] - prices[i])
            i += 1 
        return profit