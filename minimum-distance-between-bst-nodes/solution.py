# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.a = 10 ** 5

        def dfs(node):
            if not node:
                return

            if node.left:
                self.a = min(self.a, abs(node.val - node.left.val))
            if node.right:
                self.a = min(self.a, abs(node.val - node.right.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.a
