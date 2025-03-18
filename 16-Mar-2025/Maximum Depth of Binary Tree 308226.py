# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(curr):
            # base
            if curr is None:
                return 0
            
            h_left = height(curr.left)
            h_right = height(curr.right)

            return max(h_left , h_right) + 1
        return height(root)