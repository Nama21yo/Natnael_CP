# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def comb(path, i, currSum):
            if currSum == target:
                ans.append(path[:])
                return
            if i >= len(candidates) or currSum > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue  # Skip duplicates
                
                path.append(candidates[j])
                comb(path, j + 1, currSum + candidates[j])
                path.pop()
        
        comb([], 0, 0)
        return ans
