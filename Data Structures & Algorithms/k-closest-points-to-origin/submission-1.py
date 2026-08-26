import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            distance = math.sqrt((x)**2 + (y)**2)
            print((distance, (x, y)))
            heapq.heappush(res, (distance, (x, y)))
        closest = heapq.nsmallest(k, res)
        final_res = []
        for nearest in closest:
            final_res.append([nearest[1][0], nearest[1][1]])
        return final_res