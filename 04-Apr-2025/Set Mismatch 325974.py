# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, arr: List[int]) -> List[int]:
        n = len(arr)
        sn1 = (n * (n + 1)) / 2;
        sn2 = sn1 *(2 * n + 1) / 3;
        sum1 = 0;
        sum2 = 0;
        
        for i in range(len(arr)):
            sum1 += arr[i]
            sum2 +=(arr[i] * arr[i])
        
        diff1 = sum1 - sn1 # x - y
        diff2 = (sum2 - sn2) / diff1 # x + y
        
        repeating = int((diff1 + diff2) / 2)
        missing = int(diff2 - repeating)
        
        return [repeating,missing]
        