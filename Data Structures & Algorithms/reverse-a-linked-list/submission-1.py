# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes = nodes[::-1]

        newHead = nodes[0]
        curr = nodes[0]
        i = 1

        while i <= len(nodes):
            if i == len(nodes):
                curr.next = None
            else:
                curr.next = nodes[i]
                curr = curr.next
            i += 1

        return newHead