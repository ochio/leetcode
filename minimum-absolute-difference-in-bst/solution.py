# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ary = []

        def dfs(node):
            if node is None:
                return
            else:
                ary.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        ary.sort()

        diff = 10 ** 5 + 1
        for i in range(len(ary)):
            if i > 0:
                diff = min(ary[i] - ary[i - 1], diff)
        return diff
