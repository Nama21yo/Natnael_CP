# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) == 1:
            return []
        n = len(changed)
        double_arr = Counter(changed)
        if double_arr[0] % 2: # if the count of zeros is odd
            return []
        
        for num in sorted(double_arr): # will get the list
            if double_arr[num] > double_arr[2 * num]:
                return []
            double_arr[2 * num] -= double_arr[num] if num else (double_arr[num] // 2)
        
        return list(double_arr.elements())