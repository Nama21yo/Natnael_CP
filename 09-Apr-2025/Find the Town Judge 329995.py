# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return n if n == 1 else -1
        trust_map = defaultdict(int)
        for row, col in trust:
            trust_map[col] += 1
            trust_map[row] -= 1
        for key in trust_map:
            if trust_map[key] == (n - 1):
                return key
        return -1