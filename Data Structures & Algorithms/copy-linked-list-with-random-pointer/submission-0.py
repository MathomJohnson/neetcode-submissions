"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hmap = {} # original node: copied node

        ptr = head
        dummy = Node(0)
        dummyHead = dummy

        while ptr:
            dummy.next = Node(ptr.val)
            dummy = dummy.next
            hmap[ptr] = dummy
            ptr = ptr.next
        dummy.next = None

        ptr = head
        dummy = dummyHead.next
        while ptr:
            if ptr.random == None:
                dummy.random = None
            else: dummy.random = hmap[ptr.random]
            ptr = ptr.next
            dummy = dummy.next

        return dummyHead.next