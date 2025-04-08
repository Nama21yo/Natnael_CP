# Problem: Range Sum of BST - https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangebst(root, low, high):
            if root is None:
                return 0
            curr_sum = 0
            if low <= root.val <= high:
                curr_sum = root.val
            left_sum = rangebst(root.left, low, high)
            right_sum = rangebst(root.right, low, high)
            return curr_sum + left_sum + right_sum
        return rangebst(root, low, high)