
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if char == '}' and stack[-1] != '{':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                stack.pop()
        return True