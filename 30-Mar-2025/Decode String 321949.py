# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = []
        current_num = 0
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Handle multi-digit numbers
            elif char == "[":
                num_stack.append(current_num)
                string_stack.append("[")
                current_num = 0
            elif char == "]":
                replace = []
                while string_stack and string_stack[-1] != "[":
                    replace.append(string_stack.pop())
                if string_stack:
                    string_stack.pop()  # Remove the opening bracket
                if num_stack:
                    num = num_stack.pop()
                    string = "".join(reversed(replace))
                    string_stack.append(num * string)
            else:
                string_stack.append(char)
        return "".join(string_stack)
