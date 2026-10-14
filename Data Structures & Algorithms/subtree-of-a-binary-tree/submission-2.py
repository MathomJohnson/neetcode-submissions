# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root and subRoot: return False
        if not subRoot and root: return False

        q = deque()
        q.append(root)
        candidates = []
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                candidates.append(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        if not candidates: return False
        for c in candidates:
            if self.isSame(c, subRoot) != False: return True
        return False
        
    def isSame(self, root1, root2):

        if root1.val != root2.val: return False

        left = True
        if root1.left and not root2.left or not root1.left and root2.left:
            return False
        elif root1.left: 
            left = self.isSame(root1.left, root2.left)

        right = True
        if root1.right and not root2.right or not root1.right and root2.right:
            return False
        elif root1.right:
            right = self.isSame(root1.right, root2.right)
        
        if left == False or right == False: return False
