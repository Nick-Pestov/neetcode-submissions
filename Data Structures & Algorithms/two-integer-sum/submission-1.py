class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        i = 0
        while i < n:
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
            i += 1