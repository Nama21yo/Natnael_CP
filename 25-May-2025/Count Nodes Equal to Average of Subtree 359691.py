# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        average_count = 0

        def dfs(root):
            nonlocal average_count
            if not root:
                return 0, 0 # sum of subtree, number of elements
            
            if not root.left and not root.right:
                average_count += 1
                return root.val, 1

            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            curr_avg = (left_sum + right_sum + root.val) // (left_count + right_count + 1)

            if curr_avg == root.val:
                average_count += 1
            
            return left_sum + right_sum + root.val , left_count + right_count + 1
        
        dfs(root)

        return average_count