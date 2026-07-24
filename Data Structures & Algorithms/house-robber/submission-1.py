class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(0, n):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            print(i, dp[i])
        return max(dp[-1], dp[-2])