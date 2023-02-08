# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        arr = []

        while pointer:
            arr.append(pointer.val)
            pointer = pointer.next

        length = len(arr)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        for i in range(length // 2):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            prev = curr
            curr = curr.next

        return dummy.next
