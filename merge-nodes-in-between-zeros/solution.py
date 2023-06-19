# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head.next
        d = head

        while h and h.next:
            if h.val == 0:
                head = head.next
                head.val = 0
            head.val += h.val
            h = h.next

        head.next = None

        return d
