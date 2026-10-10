# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: return False
        
        fast, slow = head.next, head

        while fast != None:

            if fast == slow: return True

            if fast.next == None: return False

            fast = fast.next.next
            slow = slow.next

        return False