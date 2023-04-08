# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = t = ListNode(0)
        t.next = head

        while head and head.next:
            while head.next and head.val == head.next.val:
                head = head.next
            if t.next == head:
                t = t.next
            else:
                t.next = head.next
            head = head.next

        return s.next
