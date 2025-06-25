# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        valid = True
        for i in range(1, k):
            if nums[i] != nums[i - 1] + 1:
                valid = False
                break
        result.append(nums[k - 1] if valid else -1)
        
        for i in range(k, n):
            if nums[i] != nums[i - 1] + 1:
                valid = False
            if nums[i - k + 1] != nums[i - k] + 1:
                valid = True
                for j in range(i - k + 2, i + 1):
                    if nums[j] != nums[j - 1] + 1:
                        valid = False
                        break
            result.append(nums[i] if valid else -1)
        
        return result