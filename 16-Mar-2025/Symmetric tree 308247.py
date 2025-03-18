# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(n_left, n_right):
            if not n_left and not n_right:
                return True
            if not n_left or not n_right:
                return False
            # check the branches of left and right
            return n_left.val == n_right.val and is_mirror(n_left.left, n_right.right) and is_mirror(n_left.right, n_right.left)
            
        return is_mirror(root.left, root.right)

            