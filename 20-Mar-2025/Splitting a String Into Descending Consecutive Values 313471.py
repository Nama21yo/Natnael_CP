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

            num = 0
            # HOW IT BECOME n ^ 2 check it
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                if not path or num == path[-1] - 1:
                    path.append(num)

                    if backtrack(path, j + 1):
                        return True
                    path.pop()  # backtrack
            return False
        return backtrack([], 0)
