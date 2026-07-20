class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return s == s[::-1]