# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def helper(arr,i,k, p1):
            if i == k + 1 or k == 0:
               return 0
            if p1:  # using flag
                sub1 = arr[i] + helper(arr,i + 1, k, False) 
                sub2 =  arr[k] + helper(arr,i, k - 1, False)
                return max(sub1, sub2)
            else:
                sub1 = helper(arr,i + 1, k, True) - arr[i]
                sub2 = helper(arr,i, k - 1, True) - arr[k]
                return min(sub1, sub2)
        val = helper(nums, 0, n - 1, True)
        return val >= 0
        