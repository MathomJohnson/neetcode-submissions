# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p and q: return False
        if not q and p: return False
        
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)

        while q1:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1.val != node2.val: return False

            if node1.left: 
                q1.append(node1.left)
                if not node2.left: return False
                q2.append(node2.left)
            elif node2.left: return False
            if node1.right: 
                q1.append(node1.right)
                if not node2.right: return False
                q2.append(node2.right)
            elif node2.right: return False

        return True