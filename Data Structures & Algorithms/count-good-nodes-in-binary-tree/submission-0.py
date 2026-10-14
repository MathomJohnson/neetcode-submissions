# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        
        greatest = root.val
        self.dfs(root, greatest)

        return self.count

    def dfs(self, node, greatest):
        if not node: return

        if node.val >= greatest:
            self.count += 1
            greatest = node.val

        self.dfs(node.left, greatest)
        self.dfs(node.right, greatest)
