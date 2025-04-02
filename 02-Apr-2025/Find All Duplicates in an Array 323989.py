# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count_num = Counter(nums)
        # remember the masking trick most of the  time for duplicate
        ans = []
        for i in range(len(nums)):
            val = abs(nums[i])
            idx = val - 1

            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                ans.append(val)
        return ans
        