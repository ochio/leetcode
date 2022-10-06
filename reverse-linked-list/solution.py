# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []

        def t(h):
            if h is None:
                return
            else:
                t(h.next)
                a.append(h.val)
                return

        t(head)

        def g(i):
            if i == len(a):
                return
            h = ListNode()
            h.val = a[i]
            i += 1
            h.next = g(i)
            return h

        return g(0)
