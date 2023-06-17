from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        s = 0
        while q:
            tmp = 0
            for _ in range(len(q)):
                node = q.popleft()
                tmp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            s = tmp
        return s
