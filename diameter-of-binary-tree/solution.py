# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def dfs(node):
            if node is None:
                return 0
            dl = dfs(node.left)
            dr = dfs(node.right)
            self.d = max(self.d, dl + dr)
            return 1 + max(dl, dr)

        dfs(root)

        return self.d
