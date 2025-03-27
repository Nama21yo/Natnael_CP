# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l = - 1
        r = len(queries) + 1
        def feasible(mid):
            n = len(nums)
            line = defaultdict(int)
            for i in range(mid):
                l , r , val = queries[i]
                line[l] += val
                line[r + 1] -= val
            
            curr_sum = 0
            for i in range(n):
                curr_sum += line[i]
                if curr_sum < nums[i]:
                    return False
            return True
        while r - l > 1:
            # I I I I I I V V V V V V V
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid
        return r if r <= len(queries) else -1 
