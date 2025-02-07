# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        j = len(arr) - 1
        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1
        
        return 0 != i and  i == j and j < n - 1
        