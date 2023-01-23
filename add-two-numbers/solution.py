# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(ll):
            n = []
            while ll is not None:
                n.append(str(ll.val))
                ll = ll.next
            return int("".join(n[::-1]))

        t = str(getNum(l1) + getNum(l2))

        def rec(ln, i):
            if i < 0:
                return
            if i > 0:
                ln.next = ListNode()
            ln.val = int(t[i])
            rec(ln.next, i - 1)
            return ln

        return rec(ListNode(), len(t) - 1)
