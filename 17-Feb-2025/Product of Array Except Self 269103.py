# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*len(nums)

        # first left multiplication
        leftProduct =  1
        for i in range(n):
            answer[i] = leftProduct
            leftProduct *= nums[i]
        # then right multiplication along updating the answer    
        rightProduct = 1
        for i in range(n - 1,-1,-1):
            answer[i] *= rightProduct
            rightProduct = rightProduct * nums[i]


        return answer       