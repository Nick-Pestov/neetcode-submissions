class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        for i in range(0, n):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            print(i, dp[i])
        print(dp)
        return max(dp[-1], dp[-2])