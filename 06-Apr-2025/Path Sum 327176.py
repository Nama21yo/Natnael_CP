# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, path,target):
            if root is None:
                return False
            path += root.val
            if root.left is None and root.right is None:
                if path == target:
                    return True
            if dfs(root.left, path, target) or dfs(root.right, path, target):
                return True
            path -= root.val
            return False
        return dfs(root, 0, targetSum)
