# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        count = 0
        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                count += pow(2, r - l, mod)
                l += 1
        return count % mod