# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insert(nums, left, right):
            if left <= right:
                mid = left + (right - left)//2
                root = TreeNode(nums[mid])
                root.left = insert(nums, left, mid - 1)
                root.right = insert(nums, mid + 1, right)
                return root
        return insert(nums, 0, len(nums) - 1)
        
       