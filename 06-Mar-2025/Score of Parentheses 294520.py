# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:  
    def scoreOfParentheses(self, s: str) -> int:  
        count = 0  
        stack = []  
        
        for c in s:  
            if c == '(':  
                stack.append(0)  
            else:   
                val = 0   
                while stack and stack[-1] != 0:  
                    val += stack.pop()    
                if stack:  
                    stack.pop()  
                val = max(2 * val, 1)    
                stack.append(val)  
         
        while stack:  
            count += stack.pop()  
        
        return count  
