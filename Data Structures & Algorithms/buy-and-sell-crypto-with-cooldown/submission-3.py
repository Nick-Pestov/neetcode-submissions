class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cases
        # do nothing or buy
        # | \            |
        # do nothing, buy     sell
        # 2 states, buying state or selling state
        # do nothing, does nothing, keeps state and doesn't change value
        # if buying, subtract current price from the current max, flip the operation (i + 1), !buying
        # if selling, add current price and force a do nothing (i + 2), !buying
        dp = {} # storage structure: (index, operation) = max_profit for caching
        def dfs(i, buying):
            # if in cache, return
            if (i, buying) in dp:
                return dp[(i, buying)]

            # make sure it doesn't go out of range
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i] # cooldown is forced
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)