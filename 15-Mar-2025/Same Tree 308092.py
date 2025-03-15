# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(4)

    print(isSameTree(tree1, tree2))
    print(isSameTree(tree1, tree3))
