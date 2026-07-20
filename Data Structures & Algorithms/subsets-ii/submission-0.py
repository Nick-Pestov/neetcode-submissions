class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = set()
        curr = []
        def dfs(i):
            if i == len(nums):
                s.add(tuple(curr.copy()))
                return
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            dfs(i + 1)
        dfs(0)
        return [list(item) for item in s]