# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) & 1:
            for v in nums1:
                ans ^= v
        if len(nums1) & 1:
            for v in nums2:
                ans ^= v
        return ans