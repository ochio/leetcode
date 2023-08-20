from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        c = 0

        while q:
            nodes = []
            vals = []
            for i in range(len(q)):
                node = q.popleft()
                nodes.append(node)
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if c % 2 == 1:
                for j in range(len(nodes)):
                    nodes[j].val = vals[len(vals) - j - 1]

            c += 1

        return root
