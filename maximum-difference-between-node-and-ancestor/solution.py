# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def dfs(node):
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            t = abs(l - r)
            self.sum += t

            return l + r + node.val

        dfs(root)
        return self.sum
