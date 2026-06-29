class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        h_i, h_j = heights[0], heights[-1]
        area = (j - i) * min(h_i, h_j)
        while i < j:
            if h_i < h_j:
                i += 1
                h_i = heights[i]
                area = max(area, (j - i) * min(h_j, h_i))
            else:
                j -= 1
                h_j = heights[j]
                area = max(area, (j - i) * min(h_j, h_i))
            
        return area