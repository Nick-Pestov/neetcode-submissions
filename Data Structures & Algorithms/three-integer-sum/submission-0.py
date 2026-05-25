class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        n = len(nums)
        res = set()
        while i < n - 2:
            j = i + 1
            while j < n - 1:
                k = j + 1
                while k < n:
                    if nums[i] + nums[j] + nums[k] == 0:
                        trip = tuple(sorted((nums[i], nums[j], nums[k])))
                        res.add(trip)
                    k += 1
                j += 1
            i += 1
        return [list(t) for t in res]