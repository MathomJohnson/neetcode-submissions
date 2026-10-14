# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.flag = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.preOrder(root, -math.inf, math.inf)
        return self.flag

    def preOrder(self, node, left, right):
        if node.val <= left or node.val >= right:
            self.flag = False
            return

        if node.left:
            self.preOrder(node.left, left, node.val)

        if node.right:
            self.preOrder(node.right, node.val, right)
