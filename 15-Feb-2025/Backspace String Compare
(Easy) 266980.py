# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def valid_index(s: str, index: int) -> int:
            backspace_count = 0
            while index >= 0:
                if s[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1
            return index
                    
        s1 = len(s) - 1
        t1 = len(t) - 1

        while s1 >= 0 or t1 >= 0:
            s1 = valid_index(s, s1)
            t1 = valid_index(t, t1)

            if s1 >= 0 and t1 >= 0 and s[s1] != t[t1]:
                return False
            if (s1 >= 0) != (t1 >= 0):
                return False

            s1 -= 1
            t1 -= 1
        return True
        