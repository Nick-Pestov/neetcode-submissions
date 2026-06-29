class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            j = i + 1
            while j < n:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                if numbers[i] + numbers[j] > target:
                    break
                j += 1
            
