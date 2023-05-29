# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue):
            if not node:
                return 0

            maxValue = max(maxValue, node.val)
            return (node.val >= maxValue) + dfs(node.left, maxValue) + dfs(node.right, maxValue)

        return dfs(root, -10 ** 5)
