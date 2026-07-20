class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers)
        while i < n + 1:
            j = i + 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            i += 1