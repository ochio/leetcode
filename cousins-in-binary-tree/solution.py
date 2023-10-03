from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append(root)

        while q:
            vals = set()
            f = False
            for _ in range(len(q)):
                node = q.popleft()
                vals.add(node.val)
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (
                        node.left.val == y and node.right.val == x
                    ):
                        f = True

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if f:
                return False
            if x in vals and y in vals:
                return True
            if x in vals or y in vals:
                return False
