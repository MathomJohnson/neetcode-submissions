# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        p = head
        count = 0
        while p:
            count += 1
            p = p.next

        rem = count - n
        if rem == 0: return head.next

        curr = head
        i = 1
        while i < rem:
            curr = curr.next
            i += 1

        if n > 1: # remove Nth node
            curr.next = curr.next.next
        else:
            curr.next = None

        return head