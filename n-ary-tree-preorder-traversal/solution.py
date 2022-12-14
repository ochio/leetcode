"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ary = []

        def dfs(node):
            if node is None:
                return
            else:
                self.ary.append(node.val)

            for i in node.children:
                dfs(i)

        dfs(root)

        return self.ary
