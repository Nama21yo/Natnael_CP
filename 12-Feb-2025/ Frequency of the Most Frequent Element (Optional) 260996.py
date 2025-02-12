# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array
        l = 0
        r = 0
        count_sum = 0
        max_frequency = 0
        
        while r < len(nums):
            count_sum += nums[r]
            r += 1
            
            # Check if the current window is valid
            while count_sum + k < nums[r - 1] * (r - l):
                count_sum -= nums[l]
                l += 1
            
            max_frequency = max(max_frequency, r - l)
        
        return max_frequency
