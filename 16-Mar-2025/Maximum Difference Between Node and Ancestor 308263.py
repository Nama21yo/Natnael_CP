# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # just find the diff of max - min
        def max_diff(curr, max_so_far, min_so_far):
            if not curr:
                return max_so_far - min_so_far
            min_so_far = min(min_so_far, curr.val)
            max_so_far = max(max_so_far, curr.val)
            left_max = max_diff(curr.left, max_so_far, min_so_far)
            right_max = max_diff(curr.right, max_so_far, min_so_far)
            
            return max(left_max, right_max)
        return max_diff(root, float("-inf"), float("inf"))
