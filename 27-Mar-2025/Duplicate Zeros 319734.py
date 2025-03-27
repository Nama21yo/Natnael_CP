# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = 0
        for num in arr:
            if num == 0:
                zeros += 1
        
        j = len(arr) - 1 + zeros
        i = len(arr) - 1

        while i != j:
            if j < len(arr):
                arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                if j < len(arr):
                    arr[j] = arr[i]
                j -= 1
            i -= 1
        