# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        h = list1
        left = list1
        i = 0
        while i < a - 1:
            left = left.next
            i += 1

        right = left
        j = i

        while j <= b:
            right = right.next
            j += 1

        left.next = list2
        while left.next:
            left = left.next
        left.next = right

        return h
