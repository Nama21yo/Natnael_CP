# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = defaultdict(lambda: -1)  # Default value is -1 for missing keys
        stack = []  # Monotonic decreasing stack
       
        for i in range(n -1, -1, -1):
            while stack and nums2[stack[-1]] <= nums2[i]:
                stack.pop()
            if stack:
                res[nums2[i]] = nums2[stack[-1]]
            else:
                res[nums2[i]] = -1
            stack.append(i)

        return [res[num] for num in nums1]