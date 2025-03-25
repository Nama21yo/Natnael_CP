# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(l, r):
            if l > r:
                return -1
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(l, mid - 1)
            return binary(mid + 1, r)
        return binary(0, len(nums) - 1)