# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.a = []

        def dfs(node):
            if not node:
                return
            self.a.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        m = 10 ** 5
        for i in range(len(self.a)):
            for j in range(i + 1, len(self.a)):
                m = min(abs(self.a[i] - self.a[j]), m)

        return m
