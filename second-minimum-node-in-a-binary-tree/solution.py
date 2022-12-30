# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()

        def dfs(node):
            if node is None:
                return
            s.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        l = sorted(list(s))

        if len(l) < 2:
            return -1
        else:
            return l[1]

