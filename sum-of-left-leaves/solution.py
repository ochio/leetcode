# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def dfs(node, isLeft):
            if node is None:
                return
            if node.left is None and node.right is None:
                if isLeft:
                    self.sum += node.val
                return
            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)

        return self.sum
