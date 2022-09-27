# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa = headA
        pb = headB

        while pa != pb:
            if pa is None:
                pa = headB
            else:
                pa = pa.next

            if pb is None:
                pb = headA
            else:
                pb = pb.next

        return pa
