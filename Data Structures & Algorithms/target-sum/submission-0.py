class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp: either add or subtract
        # dp[i][ways] = dp[i + 1]
        # recurence: dp[i][ways] = dp[i]
        n = len(nums)
        t = sum(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        return dp[n][target]