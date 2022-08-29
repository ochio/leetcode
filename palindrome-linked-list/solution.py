# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        t = []
        c = head
        while (c.next is not None):
            t.append(c.val)
            c = c.next
        t.append(c.val)

        s = "".join([str(_) for _ in t])
        r = s[::-1]
        return s == r
