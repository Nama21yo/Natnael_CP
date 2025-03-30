# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    # TC- O(logn)
    # SC- O(1)
    def hIndex(self, citations):
        left, right = 0, len(citations) - 1
        n = len(citations)
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            index = n - mid
            
            if citations[mid] >= index:
                ans = index
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
