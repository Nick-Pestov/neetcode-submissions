class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = res = 0
        for char in range(len(s)):
            while s[char] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[char])
            res = max(res, char - l + 1)
        return res