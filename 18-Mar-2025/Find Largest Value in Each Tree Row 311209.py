# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)

        curr_level = 0
        max_level = []
        while queue:
            len_q = len(queue)
            maxi = float("-inf")
            for _ in range(len_q):
                curr_node = queue.popleft()
                maxi = max(curr_node.val, maxi)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                
            max_level.append(maxi)
            maxi = float("-inf")
            curr_level += 1
        
        return max_level