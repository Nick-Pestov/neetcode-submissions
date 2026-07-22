class MedianFinder:
    import heapq

    def __init__(self):
        self.small = [] # max heap for bottom half
        self.large = [] # min heap for top half

    def addNum(self, num: int) -> None:
        if len(self.large) == 0 or self.large[0] < num:
            heapq.heappush(self.large, num)
            while len(self.large) > len(self.small):
                heapq.heappush(self.small, -heapq.heappop(self.large))
        else:
            heapq.heappush(self.small, -num)
            while len(self.small) > len(self.large):
                heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] + -self.small[0])/2