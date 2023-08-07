# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head.next
        d = head

        while right:
            v = math.gcd(left.val, right.val)
            node = ListNode(val=v)
            left.next = node
            node.next = right
            left = left.next.next
            right = right.next

        return d
