class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            half = (l + r)//2 + 1
            if nums[half] == target:
                return half
            elif nums[half] < target:
                r = half
            else:
                l = half
        return -1