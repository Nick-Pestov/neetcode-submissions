import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        # build max heap
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones) # -6
            stone2 = heapq.heappop(stones) # -4
            if stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2) # push -2 (-6 - -4)
        if len(stones) == 0:
            return 0
        else:
            return -stones[-1]

