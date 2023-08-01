# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for _ in range(m)]

        top = 0
        right = n
        bottom = m
        left = 0

        while head:
            for r in range(left, right):
                if head:
                    mat[top][r] = head.val
                    head = head.next
                else:
                    break
            top += 1

            for b in range(top, bottom):
                if head:
                    mat[b][right - 1] = head.val
                    head = head.next
                else:
                    break
            right -= 1

            for l in range(right - 1, left - 1, -1):
                if head:
                    mat[bottom - 1][l] = head.val
                    head = head.next
                else:
                    break
            bottom -= 1

            for t in range(bottom - 1, top - 1, -1):
                if head:
                    mat[t][left] = head.val
                    head = head.next
                else:
                    break
            left += 1

        return mat
