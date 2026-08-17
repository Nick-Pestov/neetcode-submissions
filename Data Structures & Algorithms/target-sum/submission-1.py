class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp: either add or subtract
        # dp[i][ways] = dp[i + 1]
        # recurence: dp[i][ways] = dp[i]
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1 # 1 way to get to 0 with 0 numbers
        for i in range(n):
            for total, count in dp[i].items():
                # to get to 0: 1 way, 2: 3 ways, -3: 2 ways
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        return dp[n][target]