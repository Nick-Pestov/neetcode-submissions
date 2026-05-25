from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counts = Counter(nums)

        sorted_items = sorted(
            nums_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [num for num, freq in sorted_items[:k]]