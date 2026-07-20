class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        length = 0
        n = len(s)
        for c in charSet:
            l = count = 0
            for r in range(n):
                if s[r] != c:
                    if k == 0:
                        while l == c:
                            l += 1
                        l += 1
                        k += 1
                    k -= 1
                length = max(length, r - l + 1)
        return length
