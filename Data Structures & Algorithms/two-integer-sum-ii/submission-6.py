class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        curr = 0
        n = len(numbers)
        while curr < n:
            tmp = target - numbers[curr]
            l, r = 0, n
            while l < r:
                print(f'L:{l} and R:{r}')
                half = (l + r) // 2
                if tmp == numbers[half]:
                    return [curr + 1, half + 1]
                elif tmp > numbers[half]:
                    l = half + 1
                else:
                    r = half
            curr += 1