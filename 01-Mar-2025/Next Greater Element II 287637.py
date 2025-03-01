# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        n = 3
        1 2 1 | 1 2 >> ignore the last element
        0 1 2 | 3 4
        """
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2 * n - 2, -1, -1): # don't include the last element
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if stack:
                ans[i % n] = nums[stack[-1]]
            stack.append(i % n)
        return ans