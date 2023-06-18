# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.m = 0

        def dfs(node, dir, count):
            if not node.left and not node.right:
                self.m = max(count, self.m)
                return

            if node.left:
                if dir == "right":
                    c = count + 1
                else:
                    self.m = max(count, self.m)
                    c = 1
                dfs(node.left, "left", c)
            if node.right:
                if dir == "left":
                    c = count + 1
                else:
                    self.m = max(count, self.m)
                    c = 1
                dfs(node.right, "right", c)
        dfs(root, "", 0)
        return self.m
