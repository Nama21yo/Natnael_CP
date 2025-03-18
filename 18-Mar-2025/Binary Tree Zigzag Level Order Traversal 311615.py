# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)
        def preorder(curr, curr_level):
            if not curr:
                return curr
            # current
            level[curr_level].append(curr.val)
            preorder(curr.left, curr_level + 1)
            preorder(curr.right, curr_level + 1)
        preorder(root, 0)
        res = []
        n = len(level)
        res = []
        for i in range(n):
            if i % 2:
                level[i].reverse()
            res.append(level[i])
        return res