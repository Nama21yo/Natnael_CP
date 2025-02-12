# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotationNeeded = k % n
        
        #reverse the whole
        self.reverse(nums, 0 , n - 1)
        # reverse from start to rotation needed - 1
        self.reverse(nums, 0, rotationNeeded - 1)
        # reverse from rotation needed to the last
        self.reverse(nums, rotationNeeded, n - 1)
    def reverse(self,nums,start,end):
        while(start <= end):
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        
        
        