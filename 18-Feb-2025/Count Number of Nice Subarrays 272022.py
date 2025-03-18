# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k) - self.atMost(nums, k - 1)
    def atMost(self,nums,k):
        left = 0
        right = 0
        countOdd = 0
        countArray = 0

        while right < len(nums):
            countOdd += nums[right] % 2

            while(countOdd > k):
                countOdd -= nums[left] % 2
                left += 1
            

            countArray += (right - left + 1)
            right += 1
        
        return countArray
        