# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        d = h = ListNode(0)
        nums.sort()

        for n in nums:
            h.next = ListNode(n)
            h = h.next

        return d.next