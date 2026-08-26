import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = Counter(tasks)
        heap = []
        queue = deque()
        time = 0
        for task, count in counters.items():
            heapq.heappush(heap, -count)
        while len(queue) > 0 or len(heap) > 0:
            time += 1
            if not heap:
                tiem = queue[0][1]
            else:
                count = heapq.heappop(heap)
                count += 1
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                item = queue.popleft()[0]
                heapq.heappush(heap, item)
        return time