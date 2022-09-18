# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.check(root)

    def check(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        elif node.left is None or node.right is None:
            return max(self.check(node.left), self.check(node.right)) + 1
        return min(self.check(node.left), self.check(node.right)) + 1
