# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # O(h)
        def lcabst(root, p, q):
            if p.val > root.val and q.val > root.val:
                return lcabst(root.right, p , q)
            elif p.val < root.val and q.val < root.val:
                return lcabst(root.left, p , q)
            return root
        return lcabst(root, p ,q)