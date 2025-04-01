# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        ans = 0
        def feasible(given_sum):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > given_sum:
                    count += 1
                    total = num
            return count <= k

        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans