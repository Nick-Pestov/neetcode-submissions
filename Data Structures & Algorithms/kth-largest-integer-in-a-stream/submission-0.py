import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._queue = nums
        heapq.heapify(self._queue)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self._queue, val)
        return heapq.nlargest(self.k, self._queue)[-1]     
