# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        ans = self.dfs(root)

        if ans == False: return False
        return True

    def dfs(self, node):
        if not node: return 1

        left, right = self.dfs(node.left), self.dfs(node.right)

        if left == False or right == False: return False
        if abs(left - right) > 1: return False

        return max(left, right) + 1