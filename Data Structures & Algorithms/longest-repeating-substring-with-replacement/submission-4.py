class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        length = 0
        n = len(s)
        for c in charSet:
            r = l = count = 0
            j = k
            while r < n:
                if s[r] != c:
                    if j == 0:
                        while s[l] == c:
                            l += 1
                        l += 1
                        j += 1
                    j -= 1
                length = max(length, r - l + 1)
                r += 1
        return length
