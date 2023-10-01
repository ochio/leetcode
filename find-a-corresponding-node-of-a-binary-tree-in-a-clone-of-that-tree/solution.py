from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque()
        q.append(cloned)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.val == target.val:
                    return node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
