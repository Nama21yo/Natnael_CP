# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        
        queue = deque()
        res = []
        queue.append(root)
        curr_level = 0
        while queue:
            len_q = len(queue)
            level_arr = []
            for _ in range(len_q):
                curr_node = queue.popleft()
                level_arr.append(curr_node)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
    
            if curr_level % 2:
                # reverse as palindrome
                l = 0
                r = len_q - 1
                while l < r:
                    temp = level_arr[l].val
                    level_arr[l].val =  level_arr[r].val
                    level_arr[r].val = temp
                    l += 1
                    r -= 1
            level_arr = []
            curr_level += 1
        
        return root




