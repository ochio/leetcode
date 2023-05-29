# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        d = ListNode()
        d.next = head
        slow = d

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast == head:
            return None

        slow.next = slow.next.next

        return head
