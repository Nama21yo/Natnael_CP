# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        visited = [False] * 10
        result = []

        def backtrack(path):
            if len(path) == n + 1:
                result.append("".join(map(str, path)))
                return

            for i in range(1, 10):
                if visited[i]: continue
                pathIndex = len(path) - 1
                if pathIndex == -1 or (
                    pattern[pathIndex] == 'I' and path[-1] < i
                ) or (
                    pattern[pathIndex] == 'D' and path[-1] > i
                ):
                    visited[i] = True
                    path.append(i)
                    backtrack(path)
                    path.pop()
                    visited[i] = False

                    if result: return  # Stop early
        
        backtrack([])
        return result[0]