# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkbst(root, mini, maxi):
            if root is None:
                return True
            return mini <= root.val and root.val <= maxi and checkbst(root.left, mini, root.val - 1) and checkbst(root.right, root.val + 1, maxi)
        return checkbst(root, float("-inf"), float("inf"))