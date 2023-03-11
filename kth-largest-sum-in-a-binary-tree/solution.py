# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        s = [0] * 10 ** 5
        self.m = 0

        def rec(node, index):
            if not node:
                return
            s[index] += node.val
            rec(node.left, index + 1)
            rec(node.right, index + 1)
            self.m = max(self.m, index + 1)

        rec(root, 0)
        t = sorted(s[:self.m])

        if len(t) < k:
            return -1
        else:
            return t[-k]
