# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)

        while l < r - 1:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid 
            else:
                l = mid
        return -1