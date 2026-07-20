class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp
        # if buying --> next operation must be sell/nothing
        # if selling --> nothing, and after buy/nothing
        # buying at i --> either dfs(i + 1, buying) or dfs(i + 1, not buying) - prices[i]
        # selling at i --> either dfs(i + 1, selling) or dfs(i + 2, not selling) + prices[i]
        # buying = True/False
        # curr position at i = max(cooldown, buying)
        dp = {} # cache: (i, buying) = profit

        def dfs(i, buying):
            # base case, when i exceeds size
            if i >= len(prices):
                return 0
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(cooldown, buy)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(cooldown, sell)
            return dp[(i, buying)]
        return dfs(0, True)