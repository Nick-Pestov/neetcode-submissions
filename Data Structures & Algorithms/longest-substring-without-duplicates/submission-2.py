class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        length = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            print("C IS:", i)
            if c in unique:
                removed_idx = unique.pop(c)
                print("removed index:", removed_idx)
                length = i - removed_idx
                print("lenghtL", length)
                for (key, idx) in unique.items():
                    if idx < removed_idx:
                        unique.pop(key)
            length += 1
            unique[c] = i
        return length