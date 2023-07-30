# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, val1, val2):
            if not node:
                return

            self.ans = max(self.ans, abs(val1 - node.val), abs(val2 - node.val))
            dfs(node.left, max(val1, node.val), min(val2, node.val))
            dfs(node.right, max(val1, node.val), min(val2, node.val))

        dfs(root, root.val, root.val)
        return self.ans
