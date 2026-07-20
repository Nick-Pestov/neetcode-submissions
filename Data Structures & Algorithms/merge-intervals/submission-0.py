class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # iterate through all , collect intervals
        # [1,3] store, if next list has any point in between, uncrease that one, otherwise append
        res = []
        for (i, j) in intervals:
            if len(res) == 0:
                res.append([i, j])
            for interval in res:
                if interval[0] <= i <= interval[1]:
                    interval[1] = max(interval[1], j)
                elif interval[0] <= j <= interval[1]:
                    interval[1] = min(interval[1], i)
                else:
                    res.append([i, j])
        return res