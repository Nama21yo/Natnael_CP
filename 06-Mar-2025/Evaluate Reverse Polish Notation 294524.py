# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set()
        operator = {"+", "-","*", "/"}

        for token in tokens:
            # Operator and Operand
            if token in operator:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    division = a / b
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(floor(division))
            else: # it is an operand
                stack.append(int(token))
        return stack.pop()
        