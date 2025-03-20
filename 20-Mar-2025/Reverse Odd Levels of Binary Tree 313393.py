# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = [root]
        odd = 0
        # ans = []
        if not root:
            return []
        while level:
            nextLevel = []
            vals = []
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                vals.append(node)
            # print(vals) # check this print for visualization
            # this is the only thing that I added
            # just as palindrome reverse
            if odd % 2:
                l = 0
                r = len(vals) - 1
                while l < r:
                    temp = vals[l].val
                    vals[l].val = vals[r].val
                    vals[r].val = temp
                    l += 1
                    r -= 1
            odd += 1

            level = nextLevel
            # ans.append(vals)
        return root


