# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def flip(self, arr: List[int], index: int) -> None:
        left, right = 0, index
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr) - 1, 0, -1):
            for j in range(1, i + 1):
                if arr[j] == i + 1:
                    self.flip(arr, j)
                    flips.append(j + 1)
                    break
            self.flip(arr, i)
            flips.append(i + 1)
        
        return flips
        