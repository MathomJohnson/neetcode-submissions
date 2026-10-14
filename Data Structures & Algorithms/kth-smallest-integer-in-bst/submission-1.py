# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        order = []
        inOrder(root, order)

        return order[k-1].val
    
def inOrder(node: Optional[TreeNode], order: List):

    if not node.left and not node.right:
        order.append(node)
        return

    if node.left:
        inOrder(node.left, order)

    order.append(node)

    if node.right:
        inOrder(node.right, order)
