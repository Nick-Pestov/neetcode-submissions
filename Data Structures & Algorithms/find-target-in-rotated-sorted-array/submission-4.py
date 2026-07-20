class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            half = (l + r) // 2
            if target == nums[half]:
                return half
            elif target >= nums[l] and target < nums[r]:
                r = half
            else:
                l = half + 1
        if nums[l] == target:
            return l
        return -1
