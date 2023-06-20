# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.c = 0

        def dfs(node):
            if not node:
                return 0, 0
            left_val, left_count = dfs(node.left)
            right_val, right_count = dfs(node.right)

            t = left_val + right_val + node.val
            c = left_count + right_count + 1

            if t // c == node.val:
                self.c += 1

            return t, c

        dfs(root)
        return self.c
