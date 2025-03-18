# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n  = len(nums)
        if len(nums) == 0:
            return 1
        # modified in-place cyclic sort
        last_pos_idx = self.partition(nums)

        for i in range(last_pos_idx):
            val = abs(nums[i])
            # the output possibly can be from 1 to j+1, 
            # we assign each value’s index to negative number. 

            # use indexing trick
            if val <= last_pos_idx:
                if nums[val - 1] > 0:
                    nums[val - 1] = -nums[val - 1]
        
        # Find the First Missing Positive
        # (1<=i<=j), then that i is the first missing positive number.
        for i in range(1, last_pos_idx + 1):
            if nums[i - 1] >= 0:
                return i
        
        return last_pos_idx + 1

    def partition(self, nums):
        # The pivot is known 0

        # remember this quick sort partition method
        l = -1
        for r in range(len(nums)):
            if nums[r] > 0:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        return l + 1
        