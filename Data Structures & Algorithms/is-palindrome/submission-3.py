class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            print(f'S[i] {s[i]} and S[j] {s[j]}')
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True