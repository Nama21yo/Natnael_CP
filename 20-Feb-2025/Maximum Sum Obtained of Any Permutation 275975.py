# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0]*(n + 1)

        for l, r in requests:
            prefix[l] += 1
            prefix[r + 1] -= 1
        
        prefix[0] = prefix[0]
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1]  + prefix[i]
        
        mod = 10**9 + 7

        # higher frequencies should be bound with larger values
        prefix.sort()
        nums.sort()
        ans = 0
        print(prefix, nums)
        for i in range(n):
            # i and i + 1 is because they are out of bound
            ans += ((nums[i] % mod) * (prefix[i + 1] % mod)) % mod
        return ans % mod
