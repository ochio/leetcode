# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, nums):
            if not node:
                return

            if not node.right and not node.left:
                self.ans += nums
                return

            if node.left:
                dfs(node.left, nums * 10 + node.left.val)
            if node.right:
                dfs(node.right, nums * 10 + node.right.val)

        dfs(root, root.val)
        return self.ans
