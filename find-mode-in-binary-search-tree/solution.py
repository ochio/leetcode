# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)

        def dfs(node):
            if node is None:
                return
            d[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        max_val = max(d.values())
        keys = [key for key in d if d[key] == max_val]

        return keys
