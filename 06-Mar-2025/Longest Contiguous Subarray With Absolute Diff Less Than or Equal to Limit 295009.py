# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec = deque() # for maximum
        inc = deque() #for min
        n = len(nums)

        l = 0
        max_len = 0
        for r in range(n):
            while dec and dec[-1] < nums[r]:
                dec.pop()
            dec.append(nums[r])
            while inc and inc[-1] > nums[r]:
                inc.pop()
            inc.append(nums[r])

            while l < n and dec[0] - inc[0] > limit:
                val = nums[l]
                if inc[0] == val:
                    inc.popleft()
                if dec[0] == val:
                    dec.popleft()
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
