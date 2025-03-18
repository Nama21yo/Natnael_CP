# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(curr, target):
            if not curr:
                return curr
            if target < curr.val:
                curr.left = delete(curr.left, target)
            elif target > curr.val:
                curr.right = delete(curr.right, target)
            else:
                # case 1 >> if it was leaf node
                if not curr.right:
                    return curr.left
                if not curr.left:
                    return curr.right
                
                # find the min from the right or
                # find the min from the left
                min_right = self.minNode(curr)
                curr.val = min_right.val

                curr.right = delete(curr.right, min_right.val)
            return curr
        return delete(root,key)