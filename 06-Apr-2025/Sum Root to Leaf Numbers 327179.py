# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root, path):
            nonlocal total
            if root is None:
                return
            path = path * 10 + root.val
            if root.left is None and root.right is None:
                total += path
            else:
                dfs(root.left, path)
                dfs(root.right, path)
            path = path // 10
        dfs(root, 0)
        return total
            