# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.check(root, 0)
        return self.count

    def check(self, node, cnt):
        if node is None:
            self.count = max(self.count, cnt)
            return
        else:
            cnt += 1

        self.check(node.left, cnt)
        self.check(node.right, cnt)
