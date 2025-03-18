# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # use a queue to get get the level
        queue = deque()
        res = []
        queue.append(root)
        curr_level = 0
        while queue:
            # track each level
            len_queue = len(queue)
            res.append([]) # satrt from zero level
            for _ in range(len_queue):
                # remove from front and add the child of it in the queue
                curr_node = queue.popleft()
                res[curr_level].append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            curr_level += 1
        return res

