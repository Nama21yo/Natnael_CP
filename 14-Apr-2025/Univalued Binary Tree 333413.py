# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        flag = True
        while queue:
            curr = queue.popleft()
            lenq = len(queue)
            if curr.left:
                flag = flag and (curr.val == curr.left.val)
                queue.append(curr.left)
            if curr.right:
                flag = flag and (curr.val == curr.right.val)
                queue.append(curr.right)
        return flag
