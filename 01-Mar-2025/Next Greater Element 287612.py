# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = defaultdict(lambda: -1)  # Default value is -1 for missing keys
        stk = []  # Monotonic decreasing stack
        # Traverse nums2 from right to left
        for i in range(n - 1, -1, -1):
            # Remove elements from stack that are <= current element
            while stk and nums2[stk[-1]] <= nums2[i]:
                stk.pop()
            # If stack is not empty, the top element is the next greater
            if stk:
                res[nums2[i]] = nums2[stk[-1]]
            # Push current index onto the stack
            stk.append(i)
        # Map results to nums1 elements
        return [res[num] for num in nums1]
