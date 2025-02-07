# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums) // 2
        # x = 0 -> n 
        x = 0
        y = n
        ans = [0]*len(nums)
        i = 0
        while i < len(nums):
            ans[i] = nums[x]
            x += 1

            ans[i + 1] = nums[y]
            y += 1

            i += 2
        return ans
        