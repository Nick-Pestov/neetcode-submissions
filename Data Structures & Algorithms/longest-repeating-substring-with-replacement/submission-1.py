class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            l = count = 0
            # increase window
            for r in range(len(s)):
                # if this character is the one we want
                if c == s[r]:
                    count += 1
                # while invalid (so overexceeded k)
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1 # salvage 1 extra
                    l += 1 # shift right 1
                res = max(res, r - l + 1)
        return res









        for c in charSet:
            count = l = 0
            for r in range(len(s)): # increase window
                if s[r] == c: # did we just add in the character
                    count += 1
                while (r - l + 1) - count > k: # are we still in the budget?
                    if s[l] == c: # if not and the char is the one we want, remove one count
                        count -= 1
                    l += 1 # shift one left to min window
                res = max(res, r - l + 1) # update max
        return res

            
