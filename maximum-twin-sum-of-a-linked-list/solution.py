# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = 0
        d = head
        while d:
            d = d.next
            l += 1

        i = 0
        stack = []
        m = 0
        while head:
            if i < l / 2:
                stack.append(head.val)
            else:
                m = max(head.val + stack.pop(), m)
            head = head.next
            i += 1

        return m
