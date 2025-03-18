# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen = {")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            # If it is Open parenthesis
            if char not in closeOpen:
                stack.append(char)
            else:
                # my stack is empty
                if not stack:
                    return False
                popped = stack.pop()
                if popped != closeOpen[char]:
                    return False
        return not stack
        
        
        