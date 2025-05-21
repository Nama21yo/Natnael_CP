# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        maxi = 0
        mask = 0
        # We'll use a sliding window approach, tracking used bits. We use bitwise OR to combine bits. If the next number has a conflicting bit (used & arr[i] != 0), shrink the window until there are no conflicts. We'll use the XOR operation to remove bits during the window shrinks.
        for right in range(n):
            while mask & nums[right]:
                mask ^= nums[left]
                left += 1
            mask |= nums[right]
            maxi = max(maxi, right - left + 1)
        return maxi
            

