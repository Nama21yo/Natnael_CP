# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        pivot = 1  

        while mid <= high:
            if nums[mid] < pivot:  
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] > pivot: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:  
                mid += 1