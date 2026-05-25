class Solution:
    def rob(self, nums: List[int]) -> int:
            n1 = 0
            n2 = 0
            for i in range(len(nums)):
                temp = max(n1 + nums[i], n2)
                n1 = n2
                n2 = temp
            return n2

                