class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_ = min(heights[l], heights[r]) * (r - l)
        while l < r:
            if heights[l] < heights[r]:
                old = heights[l]
                l += 1
                while heights[l] < old and l < r:
                    l += 1
                max_ = max(min(heights[l], heights[r]) * (r - l), max_)
            else:
                old = heights[r]
                r -= 1
                while heights[r] < old and l < r:
                    r -= 1
                max_ = max(min(heights[l], heights[r]) * (r - l), max_)
        return max_