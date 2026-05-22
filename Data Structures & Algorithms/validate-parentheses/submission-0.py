class Solution:
    def isValid(self, s: str) -> bool:
        paren = {")": "(", "}": "{", "]":"["}
        stack = []
        for char in s:
            if char in paren:
                if stack and paren[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        return len(stack) == 0