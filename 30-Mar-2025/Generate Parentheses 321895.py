# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subsets = []
        def backtrack(path, i, open, close):
            if i == 2 * n:
                subsets.append("".join(path))
                return
            if open < n:
                path.append("(")
                backtrack(path, i + 1, open + 1, close)
                path.pop()
            if close < open:
                path.append(")")
                backtrack(path, i + 1, open, close + 1)
                path.pop()

        backtrack([], 0, 0, 0)
        return subsets