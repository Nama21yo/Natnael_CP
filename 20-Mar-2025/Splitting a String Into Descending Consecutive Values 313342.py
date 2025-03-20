# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(path, i):
            # if we have reached the end of the string
            if i == len(s):
                for j in range(1, len(path)):
                    if path[j] + 1 != path[j - 1]:
                        return False
                return len(path) >= 2 

            if len(path) > 2:
                for k in range(1, len(path) - 1):
                    if path[k - 1] - path[k] != 1:
                        return False

            num = 0
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                path.append(num)

                if backtrack(path, j + 1):
                    return True
                path.pop()  # backtrack
            return False
        return backtrack([], 0)
