from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        open_b = ['(','[','{']
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = deque()
        for char in s:
            if char in open_b:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        