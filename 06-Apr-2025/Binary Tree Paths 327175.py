# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def binarypath(root,path):
            if root is None:
                return
            path.append(str(root.val))
            if root.left is None and root.right is None:
                paths.append("->".join(path))
            else:
                binarypath(root.left, path)
                binarypath(root.right, path)
            path.pop()
        binarypath(root, [])
        return paths