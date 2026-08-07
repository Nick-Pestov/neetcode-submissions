class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = max(piles) # max upperbound
        j = 1
        while j < i:
            hours = 0
            k = (i + j) // 2
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours > h: # increase size
                j = k + 1
            else:
                i = k
        return j
