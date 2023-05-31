# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from sys import maxsize


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        m = -maxsize
        l = 0
        ans = 0

        while q:
            s = 0
            l += 1
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if m < s:
                ans = l
                m = s

        return ans
