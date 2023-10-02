from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        s = set()

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                s.add(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(s) > 1:
                return False

        return True
