"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if node is None:
                return 0

            m = 0
            for i in node:
                m = max(m, dfs(i.children))

            return 1 + m

        if root is None:
            return 0

        return dfs(root.children)
