# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        d = 1
        t = head

        while t.next:
            t = t.next
            d += 1

        c = d - k % d
        t.next = head
        while c > 0:
            c -= 1
            t = t.next

        a = t.next
        t.next = None

        return a
