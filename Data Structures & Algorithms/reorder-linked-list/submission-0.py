# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast, slow = head.next, head

        while fast:
            if not fast.next:
                break
            elif not fast.next.next:
                fast = None
            elif fast.next.next:
                fast = fast.next.next

            slow = slow.next

        head2 = slow.next
        slow.next = None

        # reverse second half
        nodes = []
        while head2:
            nodes.append(head2)
            head2 = head2.next
        nodes = nodes[::-1]

        # interleave
        dummy = ListNode()
        dummyCpy = dummy

        for i in range(len(nodes)):
            dummy.next = head
            dummy = dummy.next
            head = head.next

            dummy.next = nodes[i]
            dummy = dummy.next

        if head: 
            dummy.next = head
            dummy.next.next = None
        else:
            dummy.next = None

        head = dummyCpy.next






