# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d = ListNode(0, head)

        leftprev, curr = d, head

        for i in range(0, left - 1):
            leftprev = curr
            curr = curr.next

        prev = None
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        leftprev.next.next = curr
        leftprev.next = prev

        return d.next
