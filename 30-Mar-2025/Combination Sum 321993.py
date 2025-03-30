# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        def backtrack(path, i, total):
            # base case
            if i >= len(candidates):
                if total == target:
                    comb.append(path[:])
                return
            if total <= target:
                total += candidates[i]
                path.append(candidates[i])
                backtrack(path, i, total)
                total -= candidates[i]
                path.pop()
            
            backtrack(path, i + 1, total)
        backtrack([], 0, 0)
        return comb