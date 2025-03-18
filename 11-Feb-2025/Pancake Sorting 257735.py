# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr), 1,-1):
            idx = arr.index(i) 
            result.extend([idx + 1, i])
            arr = arr[:idx:-1] + arr[:idx]
        return result


        