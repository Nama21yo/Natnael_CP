# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:  
    def pivotIndex(self, arr):  
       n = len(arr)

       rightSum = sum(arr)
       leftSum = 0
       
       for i in range(n):
            rightSum -= arr[i]

            if rightSum == leftSum:
                return i
            
            leftSum += arr[i]
       return -1