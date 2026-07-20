class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = curr = res = 0
        n = len(s)
        while i  < n:
            if j < n - 1 and s[j] not in s[i:j]:
                j += 1
                curr += 1
                res = max(res, curr)
            else:
                i += 1
                curr -= 1
        return res