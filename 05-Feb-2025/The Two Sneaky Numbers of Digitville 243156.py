# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Offset zeros by 1
        nums = [num + 1 for num in nums]
        sneaky = []
        
        for i in range(len(nums)):
            val = abs(nums[i]) 
            if nums[val] > 0:
                nums[val] = -nums[val]  # Mark it as visited
            else:
                sneaky.append(val - 1)  
        
        return sneaky