class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1 = sorted(s1)
        i = 0
        while i + s1_len < s2_len:
            sub = s2[i: i + s1_len]
            sub = sorted(sub)
            if sub == s1:
                return True
            i += 1
        return False