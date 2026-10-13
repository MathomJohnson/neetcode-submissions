# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.best = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right: return 0
        self.dfs(root)
        return self.best

    def dfs(self, node: Optional[Tree]):

        if not node: return 0

        left, right = self.dfs(node.left), self.dfs(node.right)
        
        self.best = max(self.best, left + right, + 1)

        return max(left, right) + 1

