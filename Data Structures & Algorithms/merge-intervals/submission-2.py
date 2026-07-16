class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # iterate through all , collect intervals
        # [1,3] store, if next list has any point in between, uncrease that one, otherwise append
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        for (i, j) in intervals:
            last = res[-1][-1] # final entry number
            if i <= last:
                res[-1][-1] = max(last, j)
            else:
                res.append([i, j])
        return res