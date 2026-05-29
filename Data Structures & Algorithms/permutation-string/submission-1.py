class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        # expand right
        r = n1 = len(s1)
        n2 = len(s2)
        while r < n2 + 1:
            print(s2[r - n1:r])
            if sorted(s2[r - n1:r]) == sorted(s1):
                return True
            r += 1
        return False
