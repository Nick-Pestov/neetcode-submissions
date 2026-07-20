class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s == t[::-1]